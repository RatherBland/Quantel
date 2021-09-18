import os

from quantel import Quantel

qt = Quantel(api_key=os.getenv("QUANTEL_API_KEY"))
goog = qt.ticker('goog')


def test_quantel_income_statement():
    assert 'GOOG' in goog.income_statement()[0]['symbol']


def test_quantel_income_statement_ttm():
    assert 'GOOG' in goog.income_statement_ttm()[0]['symbol']


def test_quantel_income_statement_growth():
    assert 'GOOG' in goog.income_statement_growth()[0]['symbol']


def test_quantel_balance_sheet():
    assert 'GOOG' in goog.balance_sheet()[0]['symbol']


def test_quantel_balance_sheet_growth():
    assert 'GOOG' in goog.balance_sheet_growth()[0]['symbol']


def test_quantel_cash_flow():
    assert 'GOOG' in goog.cash_flow()[0]['symbol']


def test_quantel_cash_flow_ttm():
    assert 'GOOG' in goog.cash_flow_ttm()[0]['symbol']


def test_quantel_cash_flow_growth():
    assert 'GOOG' in goog.cash_flow_growth()[0]['symbol']


def test_quantel_ratios():
    assert 'GOOG' in goog.ratios()[0]['symbol']


def test_quantel_enterprise_values():
    assert 'GOOG' in goog.enterprise_values()[0]['symbol']


def test_quantel_key_metrics():
    assert 'GOOG' in goog.key_metrics()[0]['symbol']


def test_quantel_analyst_estimates():
    assert 'GOOG' in goog.analyst_estimates()[0]['symbol']


def test_quantel_shares_float():
    assert 'GOOG' in goog.shares_float()[0]['symbol']


def test_quantel_quote():
    assert 'GOOG' in goog.quote()[0]['symbol']


def test_quantel_profile():
    assert 'GOOG' in goog.profile()[0]['symbol']


def test_quantel_insider_transactions():
    assert 'GOOG' in goog.insider_transactions()[0]['symbol']


def test_quantel_insider_transactions_summarized():
    assert 'GOOG' in goog.insider_transactions_summarized()[0]['symbol']


def test_quantel_share_ownership():
    assert 'GOOG' in goog.share_ownership()[0]['symbol']


def test_quantel_historical_price():
    assert 'GOOG' in goog.historical_price()[0]['symbol']


async_goog = qt.ticker('goog', asynchronous=True)


def test_quantel_async_profile():
    assert 'GOOG' in async_goog.profile()[0]['symbol']