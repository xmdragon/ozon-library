import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "indexes" / "finance-accrual-types.json"


class FinanceAccrualTypesCatalogTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
        cls.entries = cls.catalog["entries"]
        cls.by_id = {entry["seller_api_type_id"]: entry for entry in cls.entries}

    def test_catalog_has_distinct_id_namespaces(self):
        namespaces = self.catalog["namespaces"]
        self.assertEqual(namespaces["seller_api_type_id"]["source"], "POST /v1/finance/accrual/types")
        self.assertEqual(
            namespaces["seller_ui_accrual_type_id"]["source"],
            "GET /api/site/self-gateway/api/accruals/types",
        )
        self.assertIn("不得互换", namespaces["warning"])

    def test_seller_api_type_ids_are_unique(self):
        ids = [entry["seller_api_type_id"] for entry in self.entries]
        self.assertEqual(len(ids), len(set(ids)))

    def test_verified_projection_mappings(self):
        expected = {
            1: ("Acquiring", "first_mile_fee_cny", None),
            66: ("RfbsGlobalAgentFee", "last_mile_delivery_fee_cny", 177),
            67: ("RfbsGlobalDelivery", "international_logistics_fee_cny", 106),
            69: ("SaleCommission", "ozon_commission_cny", 14),
        }
        for type_id, (name, field, ui_id) in expected.items():
            with self.subTest(type_id=type_id):
                entry = self.by_id[type_id]
                self.assertEqual(entry["seller_api_name"], name)
                self.assertEqual(entry["projection_field"], field)
                self.assertEqual(entry["seller_ui_accrual_type_id"], ui_id)

    def test_unknown_api_names_are_not_guessed(self):
        for type_id in (10, 30):
            with self.subTest(type_id=type_id):
                entry = self.by_id[type_id]
                self.assertIsNone(entry["seller_api_name"])
                self.assertNotEqual(entry["evidence_status"], "verified_by_types_api")

    def test_production_database_limit_is_explicit(self):
        observation = self.catalog["production_database_observation"]
        self.assertFalse(observation["stores_seller_api_type_id"])
        self.assertFalse(observation["has_type_reference_table"])
        self.assertEqual(observation["distinct_fee_keys"], 31)
        self.assertEqual(len(self.catalog["observed_database_fee_keys"]), 31)

    def test_production_unknown_type_ids_are_cataloged(self):
        expected = {
            29: "LastMileCourier",
            32: "Logistic",
            93: "DefectFineErrors",
        }
        for type_id, name in expected.items():
            with self.subTest(type_id=type_id):
                entry = self.by_id[type_id]
                self.assertEqual(entry["seller_api_name"], name)
                self.assertEqual(entry["projection_status"], "needs_policy")
                self.assertIn(f"accrual:{type_id}", entry["fee_key"])

    def test_projection_fields_use_known_posting_columns(self):
        allowed = {
            None,
            "ozon_commission_cny",
            "last_mile_delivery_fee_cny",
            "international_logistics_fee_cny",
            "first_mile_fee_cny",
            "compensation_cny",
            "refund_cny",
            "error_fee_cny",
        }
        self.assertTrue(all(entry["projection_field"] in allowed for entry in self.entries))


if __name__ == "__main__":
    unittest.main()
