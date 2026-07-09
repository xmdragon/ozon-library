import json
import tempfile
import unittest
from pathlib import Path

from tools.generate_official_api_docs import (
    generate_docs,
    operation_group,
    render_operation_doc,
    slugify_operation,
)


def sample_operation(path="/v3/product/list", operation_id="ProductAPI_GetProductList", title="商品列表"):
    return {
        "title": title,
        "method": "post",
        "path": path,
        "operationId": operation_id,
        "sourceUrl": f"https://docs.ozon.ru/api/seller/zh/#operation/{operation_id}",
        "headings": ["商品列表", "header Parameters", "Request Body schema", "Response Schema"],
        "tables": [
            {"index": 0, "text": "Client-Id required string 用户识别号。 Api-Key required string API-密钥。"},
            {"index": 1, "text": "filter object 过滤器。 limit integer 每页数量。"},
            {"index": 2, "text": "result object 商品结果。 total integer 总数。"},
        ],
        "examples": [
            {"index": 0, "text": '{"filter": {"visibility": "ALL"}, "limit": 10}'},
            {"index": 1, "text": '{"result": {"items": []}, "total": 0}'},
        ],
    }


class GenerateOfficialApiDocsTest(unittest.TestCase):
    def test_slug_includes_method_path_and_operation_id(self):
        slug = slugify_operation(sample_operation())

        self.assertEqual(slug, "post-v3-product-list-ProductAPI_GetProductList.md")

    def test_group_uses_first_stable_path_segment(self):
        self.assertEqual(operation_group(sample_operation()), "product")
        self.assertEqual(operation_group(sample_operation("/v4/posting/fbs/list", "PostingFbsList")), "posting")

    def test_render_operation_doc_contains_official_details(self):
        doc = render_operation_doc(sample_operation())

        self.assertIn("# 商品列表", doc)
        self.assertIn("`POST /v3/product/list`", doc)
        self.assertIn("`ProductAPI_GetProductList`", doc)
        self.assertIn("- `Client-Id` required string - 用户识别号。", doc)
        self.assertIn("- `Api-Key` required string - API-密钥。", doc)
        self.assertIn("- `filter` object - 过滤器。", doc)
        self.assertIn("- `limit` integer - 每页数量。", doc)
        self.assertIn(
            '```json\n{\n  "filter": {\n    "visibility": "ALL"\n  },\n  "limit": 10\n}\n```',
            doc,
        )
        self.assertIn("https://docs.ozon.ru/api/seller/zh/#operation/ProductAPI_GetProductList", doc)

    def test_render_operation_doc_splits_collapsed_schema_fields(self):
        operation = sample_operation()
        operation["tables"] = [
            {
                "index": 0,
                "text": (
                    "resultArray of objects 请求结果。 Array ()idnumber 活动识别号。 "
                    "titlestring 活动名称。 action_typestring 活动类型。 "
                    "is_participatingboolean 无论你是否参加这项活动。"
                ),
            }
        ]

        doc = render_operation_doc(operation)

        self.assertIn("- `result` Array of objects - 请求结果。", doc)
        self.assertIn("- `id` number - 活动识别号。", doc)
        self.assertIn("- `title` string - 活动名称。", doc)
        self.assertIn("- `action_type` string - 活动类型。", doc)
        self.assertIn("- `is_participating` boolean - 无论你是否参加这项活动。", doc)
        self.assertNotIn("resultArray of objects 请求结果。 Array ()idnumber", doc)
        self.assertNotIn("Array ()", doc)

    def test_render_operation_doc_splits_required_schema_fields(self):
        operation = sample_operation()
        operation["tables"] = [
            {
                "index": 0,
                "text": (
                    "date_end required string <date-time> 促销活动结束日期与时间。 "
                    "date_start required string <date-time> 促销活动开始日期与时间。 "
                    "min_action_percent required number <double> 最低折扣百分比。 "
                    "titlestring [ 1 .. 256 ] characters 促销活动名称。"
                ),
            }
        ]

        doc = render_operation_doc(operation)

        self.assertIn("- `date_end` required string <date-time> - 促销活动结束日期与时间。", doc)
        self.assertIn("- `date_start` required string <date-time> - 促销活动开始日期与时间。", doc)
        self.assertIn("- `min_action_percent` required number <double> - 最低折扣百分比。", doc)
        self.assertIn("- `title` string - [ 1 .. 256 ] characters 促销活动名称。", doc)
        self.assertNotIn("titlestring", doc)

    def test_render_operation_doc_prefers_structured_table_rows(self):
        operation = sample_operation()
        operation["tables"] = [
            {
                "index": 0,
                "text": "Client-Id required string 用户识别号。 Api-Key required string API-密钥。",
                "rows": [
                    ["Client-Id required", "string 用户识别号。"],
                    ["Api-Key required", "string API-密钥。"],
                ],
            },
            {
                "index": 1,
                "text": "resultArray of objects 请求结果。 Array ()idnumber 活动识别号。",
                "rows": [
                    ["result", "Array of objects 请求结果。"],
                    ["Array ()idnumber <double> 活动识别号。 titlestring 活动名称。"],
                    ["id", "number <double> 活动识别号。"],
                ],
            },
        ]

        doc = render_operation_doc(operation)

        self.assertIn("| 字段 | 类型/说明 |", doc)
        self.assertIn("| `Client-Id` required | string 用户识别号。 |", doc)
        self.assertIn("| `Api-Key` required | string API-密钥。 |", doc)
        self.assertIn("| `result` | Array of objects 请求结果。 |", doc)
        self.assertIn("| `id` | number <double> 活动识别号。 |", doc)
        self.assertNotIn("resultArray of objects", doc)
        self.assertNotIn("Array ()idnumber", doc)

    def test_render_operation_doc_shows_lifecycle_and_news_updates(self):
        operation = sample_operation("/v1/review/list", "ReviewAPI_ReviewList", "评价列表")
        operation["lifecycle"] = {
            "status": "deprecated",
            "date": "2026-06-11",
            "replacement_paths": ["/v2/review/list"],
            "sourceUrl": "https://docs.ozon.ru/api/seller/zh/#section/2026611",
            "text": "/v1/review/list 该方法已弃用，并将在未来停用。请切换到/v2/review/list。",
        }
        operation["news_updates"] = [
            {
                "date": "2026-06-11",
                "labels": ["deprecated_method"],
                "text": "/v1/review/list 该方法已弃用，并将在未来停用。请切换到/v2/review/list。",
                "sourceUrl": "https://docs.ozon.ru/api/seller/zh/#section/2026611",
            },
            {
                "date": "2026-07-08",
                "labels": ["graduated"],
                "text": "/v1/review/list 已将该方法从Beta版迁移至正式版。",
                "sourceUrl": "https://docs.ozon.ru/api/seller/zh/#section/202678",
            },
        ]

        doc = render_operation_doc(operation)

        self.assertIn("> [!WARNING]", doc)
        self.assertIn("官方 News 标记此方法为 `deprecated`", doc)
        self.assertIn("替代方法：`/v2/review/list`", doc)
        self.assertIn("## News 更新标记", doc)
        self.assertIn("| 2026-06-11 | `deprecated_method` |", doc)
        self.assertIn("/v1/review/list 该方法已弃用", doc)

    def test_generate_docs_writes_readme_and_one_file_per_operation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            index_path = root / "official.json"
            output_dir = root / "official"
            operations = [
                sample_operation(),
                sample_operation(
                    "/v1/finance/realization",
                    "FinanceAPI_GetRealizationReport",
                    "实现报告",
                ),
            ]
            index_path.write_text(
                json.dumps({"operations": operations, "operation_count": 2}, ensure_ascii=False),
                encoding="utf-8",
            )

            count = generate_docs(index_path, output_dir)

            self.assertEqual(count, 2)
            readme = (output_dir / "README.md").read_text(encoding="utf-8")
            self.assertIn("官方 Seller API 方法文档", readme)
            self.assertIn("[商品列表](post-v3-product-list-ProductAPI_GetProductList.md)", readme)
            self.assertIn(
                "[实现报告](post-v1-finance-realization-FinanceAPI_GetRealizationReport.md)",
                readme,
            )
            self.assertTrue((output_dir / "post-v3-product-list-ProductAPI_GetProductList.md").exists())
            self.assertTrue((output_dir / "post-v1-finance-realization-FinanceAPI_GetRealizationReport.md").exists())


if __name__ == "__main__":
    unittest.main()
