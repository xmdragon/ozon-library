# 策略信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/pricing-strategy/info`
- Operation ID：`pricing_info`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/pricing_info
- 分组：`pricing-strategy`

## 页面标题结构

- 策略信息
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
| `strategy_id` required | string 策略ID。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | object 方法操作结果。 |
| `competitors` | Array of objects 竞争对手列表。 |
| `enabled` | boolean 策略状态： true —— 打开， false —— 关闭。 |
| `name` | string 策略名称。 |
| `type` | string 策略类型： MIN_EXT_PRICE —— 系统策略， COMP_PRICE —— 用户策略。 |
| `update_type` | string 上次策略更改的类型： strategyEnabled —— 恢复， strategyDisabled —— 停止， strategyChanged —— 更新， strategyCreated —— 创建， strategyItemsListChanged —— 策略中的商品集合已更改。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `competitors` | Array of objects 竞争对手列表。 |
| `enabled` | boolean 策略状态： true —— 打开， false —— 关闭。 |
| `name` | string 策略名称。 |
| `type` | string 策略类型： MIN_EXT_PRICE —— 系统策略， COMP_PRICE —— 用户策略。 |
| `update_type` | string 上次策略更改的类型： strategyEnabled —— 恢复， strategyDisabled —— 停止， strategyChanged —— 更新， strategyCreated —— 创建， strategyItemsListChanged —— 策略中的商品集合已更改。 |

## 示例

### 示例 0

```text
true
```

### 示例 1

```text
false
```

### 示例 2

```text
MIN_EXT_PRICE
```

### 示例 3

```text
COMP_PRICE
```

### 示例 4

```text
strategyEnabled
```

### 示例 5

```text
strategyDisabled
```

### 示例 6

```text
strategyChanged
```

### 示例 7

```text
strategyCreated
```

### 示例 8

```text
strategyItemsListChanged
```

### 示例 9

```json
{"strategy_id": "2fb3e6a3-3db5-4bb4-8430-b2de39fc3265"}
```

### 示例 10

```json
{"result": {"strategy_name": "策略_来自_CID7","enabled": true,"update_type": "strategyItemsListChanged","type": "COMP_PRICE","competitors": [{"competitor_id": 204,"coefficient": 1},{"competitor_id": 1008426,"coefficient": 1}]}}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。
