# 将快递方式与快递设施联系起来

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/polygon/bind`
- Operation ID：`PolygonAPI_BindPolygon`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PolygonAPI_BindPolygon
- 分组：`polygon`

## 页面标题结构

- 将快递方式与快递设施联系起来
- header Parameters
- Request Body schema: application/json
- 回复
- Response Schema: application/json
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
| `delivery_method_id` required | integer <int32> 快递方法识别号。 |
| `polygons` required | Array of objects 设施清单。 |
| `warehouse_location` required | object 仓库位置。 |

## 示例

### 示例 0

```json
{"delivery_method_id": 0,"polygons": [{"polygon_id": "1323","time": "30"}],"warehouse_location": {"lat": "58.52391272075821","lon": "31.236791610717773"}}
```

### 示例 1

```json
{ }
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。
