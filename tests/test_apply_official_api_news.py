import copy
import unittest

from tools.apply_official_api_news import apply_news_metadata, extract_paths, summarize_news_entry


class ApplyOfficialApiNewsTest(unittest.TestCase):
    def test_extract_paths_splits_concatenated_versioned_paths(self):
        text = "/v3/posting/fbs/list/v3/posting/fbs/unfulfilled/list 已更新。"

        self.assertEqual(
            extract_paths(text),
            ["/v3/posting/fbs/list", "/v3/posting/fbs/unfulfilled/list"],
        )

    def test_summarize_entry_detects_deprecated_and_new_methods(self):
        entry = {
            "date": "2026-06-11",
            "id": "section/2026611",
            "sourceUrl": "https://docs.ozon.ru/api/seller/zh/#section/2026611",
            "text": (
                "2026年6月11日 方法 变更 /v2/review/list 新增了用于获取评价列表的方法版本。 "
                "/v1/review/list 该方法已弃用，并将在未来停用。请切换到/v2/review/list。"
            ),
        }

        summaries = summarize_news_entry(entry)
        by_path = {item["path"]: item for item in summaries}

        self.assertIn("new_method", by_path["/v2/review/list"]["labels"])
        self.assertIn("deprecated_method", by_path["/v1/review/list"]["labels"])
        self.assertEqual(by_path["/v1/review/list"]["replacement_paths"], ["/v2/review/list"])

    def test_apply_news_metadata_marks_only_deprecated_source_method(self):
        operations = [
            {"path": "/v1/review/list", "operationId": "ReviewAPI_ReviewList"},
            {"path": "/v2/review/list", "operationId": "ReviewListV2"},
            {"path": "/v1/product/prices/details", "operationId": "ProductPricesDetails"},
        ]
        news = {
            "entries": [
                {
                    "date": "2026-06-11",
                    "id": "section/2026611",
                    "sourceUrl": "https://docs.ozon.ru/api/seller/zh/#section/2026611",
                    "text": (
                        "2026年6月11日 方法 变更 /v2/review/list 新增了用于获取评价列表的方法版本。 "
                        "/v1/review/list 该方法已弃用，并将在未来停用。请切换到/v2/review/list。"
                    ),
                },
                {
                    "date": "2026-05-19",
                    "id": "section/2026519",
                    "sourceUrl": "https://docs.ozon.ru/api/seller/zh/#section/2026519",
                    "text": (
                        "2026年5月19日 方法 变更 /v1/product/prices/details 在方法响应中："
                        "新增了prices.price_indexes参数；将prices.discount_percent参数标记为已弃用。"
                    ),
                },
                {
                    "date": "2026-06-09",
                    "id": "section/202669",
                    "sourceUrl": "https://docs.ozon.ru/api/seller/zh/#section/202669",
                    "text": "2026年6月9日 方法 变更 /v2/chat/list 该方式已过期，我们已将其从文件中删除。请使用 /v3/chat/list。",
                },
            ]
        }

        result = apply_news_metadata(copy.deepcopy(operations), news)
        by_path = {operation["path"]: operation for operation in result["operations"]}

        self.assertEqual(by_path["/v1/review/list"]["lifecycle"]["status"], "deprecated")
        self.assertEqual(by_path["/v1/review/list"]["lifecycle"]["replacement_paths"], ["/v2/review/list"])
        self.assertNotIn("lifecycle", by_path["/v2/review/list"])
        self.assertIn("new_method", by_path["/v2/review/list"]["news_updates"][0]["labels"])
        self.assertIn("added_field", by_path["/v1/product/prices/details"]["news_updates"][0]["labels"])
        self.assertIn("deprecated_field", by_path["/v1/product/prices/details"]["news_updates"][0]["labels"])
        self.assertNotIn("lifecycle", by_path["/v1/product/prices/details"])
        self.assertEqual(result["removed_or_missing_methods"][0]["path"], "/v2/chat/list")

    def test_field_only_removal_does_not_mark_operation_removed(self):
        operations = [{"path": "/v3/product/info/list", "operationId": "ProductInfoList"}]
        news = {
            "entries": [
                {
                    "date": "2025-11-12",
                    "id": "section/20251112",
                    "sourceUrl": "https://docs.ozon.ru/api/seller/zh/#section/20251112",
                    "text": (
                        "2025年11月12日 方法 变更 /v3/product/info/list "
                        "在方法回答该items.marketing_price参数已过期，我们已将其从文件中删除。"
                    ),
                }
            ]
        }

        result = apply_news_metadata(copy.deepcopy(operations), news)
        operation = result["operations"][0]

        self.assertNotIn("lifecycle", operation)
        self.assertIn("removed_field", operation["news_updates"][0]["labels"])
        self.assertNotIn("removed_method", operation["news_updates"][0]["labels"])


if __name__ == "__main__":
    unittest.main()
