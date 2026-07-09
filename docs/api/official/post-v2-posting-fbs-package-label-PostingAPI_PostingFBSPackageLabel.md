# 打印标签

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/posting/fbs/package-label`
- Operation ID：`PostingAPI_PostingFBSPackageLabel`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PostingAPI_PostingFBSPackageLabel
- 分组：`posting`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-03-10 | `updated` | /v2/posting/fbs/package-label 更新了方法描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2026310) |
| 2025-09-24 | `updated` | /v2/posting/fbs/package-label 更新了方法描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2025924) |

## 页面标题结构

- 打印标签
- header Parameters
- Request Body schema: application/json
- 回复
- Response Schema: application/pdf
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `Client-Id` required | string 用户识别号。 |
| `Api-Key` required | string API-密钥。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `posting_number` required | Array of strings 货运ID。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `file_content` | string <byte> 二进制形式的文件内容。 |
| `file_name` | string 文件名称。 |
| `content_type` | string 文件类型。 |

## 示例

### 示例 0

```text
The next postings aren't ready
```

### 示例 1

```json
{
  "posting_number": [
    "48173252-0034-4"
  ]
}
```

### 示例 2

```json
{
  "content_type": "application/pdf",
  "file_name": "ticket-170660-2023-07-13T13:17:06Z.pdf",
  "file_content": "%PDF-1.7\n%âãÏÓ\n53 0 obj\n<</MarkInfo<</Marked true/Type/MarkInfo>>/Pages 9 0 R/StructTreeRoot 10 0 R/Type/Catalog>>\nendobj\n8 0 obj\n<</Filter/FlateDecode/Length 2888>>\nstream\nxå[[ݶ\u0011~?¿BÏ\u0005Bs\u001c^\u0000Àwí5ú\u0010 m\u0016Èsà¦)\n;hÒ\u0014èÏïG\u0014)<{äµ] ]?¬¬oIÎ}¤F±óϤñï\u001bÕü×X­´OÏï?^~¹$<ø¨È9q\u0013Y\u0012åñì§_¼|ÿégü\t+\u0012\u001bxª}Æxҿ¿¼_º¼xg¦þ5OkuÌ3ýíògüûå\"Ni\u0016C\u0001°\u000fA9g'r¢\"\u0013YóĪ\u0018NÑ{\u001dÕóZ¬\\Ô\""
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。
