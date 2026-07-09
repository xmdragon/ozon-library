# 货位标签

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/posting/fbs/act/get-container-labels`
- Operation ID：`PostingAPI_PostingFBSActGetContainerLabels`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PostingAPI_PostingFBSActGetContainerLabels
- 分组：`posting`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-06-03 | `new_method` | /v2/posting/fbs/act/get-container-labels 新增了方法，用于创建货位标签。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/202663) |

## 页面标题结构

- 货位标签
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
| `id` required | integer <int64> 来自方法/v1/carriage/create的文件生成任务编号（也是运输标识符）。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `file_content` | string <byte> 文件内容，以二进制形式。 |
| `file_name` | string 文件名称。 |
| `content_type` | string 文件类型。 |

## 示例

### 示例 0

```json
{
  "id": 295662811
}
```

### 示例 1

```json
{
  "content_type": "application/pdf",
  "file_name": "carriage-containers-20903594.pdf",
  "file_content": "%PDF-1.4\n%âãÏÓ\n2 0 obj\n<</Length 2992/Filter/FlateDecode>>stream\nxµ}[ێ\u001c·\u0011}¯èç\u0000¦Èb\u0015/ @»+\u0019y0Ë\u0002ù\u0000%q\u0010X\u0001ìü?Ãn²ÉéfÍì(ò®\u001duMÝ/<Å\u0019\u001bòyýY,0Ã?=[ccyýåëå×K¡§\u000bAÂâ؉x\u001dßþqùÛ\u001fÿà-dp¢UÔø\u001aün)¿ùqÙ^üöóåݏùù¿«X¶i\t²JúçåÏøýõÙ$Gxn²\u0011&\u000f¥ÉCj¾§2aæºr&­^,~hI²)F¤ù7¥íu£:oÊ\u0013Ùȹ0ûLdB\u001a\u0018y§xk;ë<^Lv)%¼)í\u0014öcyóÎX:\u0018ÚõIXå\u0015\u0013╏\rõɌ5dýÆ\u0016Ê!6Ñpys\u001aÄXYÃ1­Ô\r:H©(%U´³bR"
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。
