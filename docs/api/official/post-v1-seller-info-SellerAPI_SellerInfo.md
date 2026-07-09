# 卖家个人中心信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/seller/info`
- Operation ID：`SellerAPI_SellerInfo`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/SellerAPI_SellerInfo
- 分组：`seller`

## 页面标题结构

- 卖家个人中心信息
- header Parameters
- 回复
- Response Schema: application/json
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
| `company` | object 公司。 |
| `ratings` | Array of objects 评级列表。 |
| `subscription` | object 订阅。 |

## 示例

### 示例 0

```json
{"company": {"country": "俄罗斯","currency": "RUB","inn": "7707083893","legal_name": "“Romashka”有限责任公司","name": "“Romashka”有限责任公司","ogrn": "1027700132195","ownership_form": "私人所有制","tax_system": "普通税制"},"ratings": [{"current_value": {"date_from": "2023-01-15T09:00:00Z","date_to": "2023-12-31T23:59:59Z","formatted": "AA+","status": {"danger": false,"premium": true,"warning": false},"value": 85},"name": "财务稳定性","past_value": {"date_from": "2022-01-01T00:00:00Z","date_to": "2022-12-31T23:59:59Z","formatted": "A","status": {"danger": false,"premium": false,"warning": true},"value": 78},"rating": "高水平","status": "活跃","value_type": "定量"}],"subscription": {"is_premium": true,"type": "专业"}}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。
