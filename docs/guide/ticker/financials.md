### **quote**

=== "Details"

    - *Description*:  Retrieves stock quote
    - *Return*:  `List[Dict]`

=== "Example"

    ```python
    from quantel import Quantel

    qt = Quantel(api_key="<your-quantel-api-key>")

    goog = qt.ticker('goog')
    goog.quote()
    ```

=== "Data"

    ```python
    [{'avgVolume': 1136007,
      'change': -8.14,
      'changesPercentage': -0.29,
      'dayHigh': 2776.955,
      'dayLow': 2747.0,
      'earningsAnnouncement': None,
      'eps': 92.187,
      'exchange': 'NASDAQ',
      'marketCap': 1827191914496.0,
      'name': 'Alphabet Inc.',
      'open': 2765.66,
      'pe': 29.871784,
      'previousClose': 2761.93,
      'price': 2753.79,
      'priceAvg200': 2325.6572,
      'priceAvg50': 2644.9353,
      'sharesOutstanding': 663518974,
      'symbol': 'GOOG',
      'timestamp': 1628770344,
      'volume': 760483,
      'yearHigh': 2800.22,
      'yearLow': 1406.55}]
    ...
    ```

### **balance_sheet**

=== "Details"

    - *Description*:  Retrieves all balance sheet statements
    - *Return*:  `List[Dict]`

=== "Example"

    ```python
    from quantel import Quantel

    qt = Quantel(api_key="<your-quantel-api-key>")

    goog = qt.ticker('goog')
    goog.balance_sheet()
    ```

=== "Data"

    ```python
    [{'acceptedDate': '2021-02-02 20:12:25',
     'accountPayables': 5589000000,
     'accumulatedOtherComprehensiveIncomeLoss': 633000000,
     'cashAndCashEquivalents': 26465000000,
     'cashAndShortTermInvestments': 136694000000,
     'commonStock': 58510000000,
     'date': '2020-12-31',
     'deferredRevenue': 2543000000,
     'deferredRevenueNonCurrent': 481000000,
     'deferredTaxLiabilitiesNonCurrent': 3561000000,
     'fillingDate': '2021-02-03',
     'goodwill': 21175000000,
     'goodwillAndIntangibleAssets': 22620000000,
     'intangibleAssets': 1445000000,
     'inventory': 728000000,
     'longTermDebt': 13932000000,
     'longTermInvestments': 20703000000,
     'netDebt': 307000000,
     'netReceivables': 31384000000,
     'otherAssets': 0,
     'otherCurrentAssets': 5490000000,
     'otherCurrentLiabilities': 10409000000,
     'otherLiabilities': 0,
     'otherNonCurrentAssets': 3953000000,
     'otherNonCurrentLiabilities': 2269000000,
     'othertotalStockholdersEquity': 0,
     'period': 'FY',
     'propertyPlantEquipmentNet': 96960000000,
     'reportedCurrency': 'USD',
     'retainedEarnings': 163401000000,
     'shortTermDebt': 0,
     'shortTermInvestments': 110229000000,
     'symbol': 'GOOG',
     'taxAssets': 1084000000,
     'taxPayables': 1485000000,
     'totalAssets': 319616000000,
     'totalCurrentAssets': 174296000000,
     'totalCurrentLiabilities': 56834000000,
     'totalDebt': 26772000000,
     'totalInvestments': 130932000000,
     'totalLiabilities': 97072000000,
     'totalLiabilitiesAndStockholdersEquity': 319616000000,
     'totalNonCurrentAssets': 145320000000,
     'totalNonCurrentLiabilities': 40238000000,
     'totalStockholdersEquity': 222544000000
    },
    ...

    ```


### **balance_sheet_growth**

=== "Details"

    - *Description*:  Retrieves balance sheet growth by percentage data
    - *Return*:  `List[Dict]`

=== "Example"

    ```python
    from quantel import Quantel

    qt = Quantel(api_key="<your-quantel-api-key>")

    goog = qt.ticker('goog')
    goog.balance_sheet_growth()
    ```

=== "Data"

    ```python
    [{'date': '2020-12-31',
     'growthAccountPayables': 0.005035065635677036,
     'growthAccumulatedOtherComprehensiveIncomeLoss': -1.5137987012987013,
     'growthCashAndCashEquivalents': 0.43069521029300467,
     'growthCashAndShortTermInvestments': 0.14221015249634428,
     'growthCommonStock': 0.15742206045260326,
     'growthDeferredRevenue': 0.3328092243186583,
     'growthDeferredRevenueNonCurrent': 0.3435754189944134,
     'growthDeferrredTaxLiabilitiesNonCurrent': 1.09347442680776,
     'growthGoodwill': 0.02671644685802948,
     'growthGoodwillAndIntangibleAssets': 0.000752112551431226,
     'growthIntangibleAssets': -0.269833249115715,
     'growthInventory': -0.27127127127127126,
     'growthLongTermDebt': 2.059288537549407,
     'growthLongTermInvestments': 0.5830402202171586,
     'growthNetDebt': -1.0220166379804934,
     'growthNetReceivables': 0.14156845627819,
     'growthOtherAssets': 0.0,
     'growthOtherCurrentAssets': 0.2443336355394379,
     'growthOtherCurrentLiabilities': -0.48257692498881544,
     'growthOtherLiabilities': 0.0,
     'growthOtherNonCurrentAssets': 0.29056480574600063,
     'growthOtherNonCurrentLiabilities': -0.9013092079509373,
     'growthOthertotalStockholdersEquity': -1.0,
     'growthPropertyPlantEquipmentNet': 0.1462754323950489,
     'growthRetainedEarnings': 0.07414443670212066,
     'growthShortTermDebt': 0.0,
     'growthShortTermInvestments': 0.08946697371932356,
     'growthTaxAssets': -0.3627278071722516,
     'growthTaxPayables': 4.41970802919708,
     'growthTotalAssets': 0.1584109253413263,
     'growthTotalCurrentAssets': 0.14234031118509877,
     'growthTotalCurrentLiabilities': 0.25680546648680924,
     'growthTotalDebt': 4.878787878787879,
     'growthTotalInvestments': 0.14596297755021662,
     'growthTotalLiabilities': 0.3035572804060859,
     'growthTotalLiabilitiesAndStockholdersEquity': 0.1584109253413263,
     'growthTotalNonCurrentAssets': 0.17829256229171903,
     'growthTotalNonCurrentLiabilities': 0.3758462695753265,
     'growthTotalStockholdersEquity': 0.10475471847976092,
     'period': 'FY',
     'symbol': 'GOOG'},
    ...

    ```

### **income_statement**

=== "Details"

    - *Description*:  Retrieves all income statements
    - *Return*:  `List[Dict]`

=== "Example"

    ```python
    from quantel import Quantel

    qt = Quantel(api_key="<your-quantel-api-key>")

    goog = qt.ticker('goog')
    goog.income_statement()
    ```

=== "Data"

    ```python
    [{'acceptedDate': '2021-02-02 20:12:25',
     'costAndExpenses': 141303000000,
     'costOfRevenue': 84732000000,
     'date': '2020-12-31',
     'depreciationAndAmortization': 13697000000,
     'ebitda': 54921000000,
     'ebitdaratio': 0.3008924707029645,
     'eps': 58.14692108710071,
     'epsdiluted': 58.14692108710071,
     'fillingDate': '2021-02-03',
     'generalAndAdministrativeExpenses': 11052000000,
     'grossProfit': 97795000000,
     'grossProfitRatio': 0.5357837470620785,
     'incomeBeforeTax': 48082000000,
     'incomeBeforeTaxRatio': 0.2634240413747007,
     'incomeTaxExpense': 7813000000,
     'interestExpense': 135000000,
     'netIncome': 40269000000,
     'netIncomeRatio': 0.22061941520980458,
     'operatingExpenses': 56571000000,
     'operatingIncome': 41224000000,
     'operatingIncomeRatio': 0.22585151785763202,
     'otherExpenses': 0,
     'period': 'FY',
     'reportedCurrency': 'USD',
     'researchAndDevelopmentExpenses': 27573000000,
     'revenue': 182527000000,
     'sellingAndMarketingExpenses': 17946000000,
     'sellingGeneralAndAdministrativeExpenses': 28998000000,
     'symbol': 'GOOG',
     'totalOtherIncomeExpensesNet': -6858000000,
     'weightedAverageShsOut': 675582000,
     'weightedAverageShsOutDil': 680794590},
    ...
    ```

### **income_statement_ttm**

=== "Details"

    - *Description*:  Retrieves income statement trailing twelve months
    - *Return*:  `List[Dict]`

=== "Example"

    ```python
    from quantel import Quantel

    qt = Quantel(api_key="<your-quantel-api-key>")

    goog = qt.ticker('goog')
    goog.income_statement_ttm()
    ```

=== "Data"

    ```python
    [{
        "symbol": "GOOG",
        "reportedCurrency": "USD",
        "period": "TTM",
        "revenueTTM": 220265000000,
        "costOfRevenueTTM": 97527000000,
        "grossProfitTTM": 122738000000,
        "researchAndDevelopmentExpensesTTM": 29038000000,
        "generalAndAdministrativeExpensesTTM": 11701000000,
        "sellingAndMarketingExpensesTTM": 19337000000,
        "sellingGeneralAndAdministrativeExpensesTTM": 31038000000,
        "otherExpensesTTM": 0,
        "operatingExpensesTTM": 60076000000,
        "costAndExpensesTTM": 157603000000,
        "interestExpenseTTM": 253000000,
        "depreciationAndAmortizationTTM": 12901000000,
        "ebitdaTTM": 88470000000,
        "operatingIncomeTTM": 62662000000,
        "totalOtherIncomeExpensesNetTTM": -12654000000,
        "incomeBeforeTaxTTM": 75316000000,
        "incomeTaxExpenseTTM": 12387000000,
        "netIncomeTTM": 62929000000
      }]
    ...
    ```

### **income_statement_growth**

=== "Details"

    - *Description*:  Retrieves income statements growth by percentage data
    - *Return*:  `List[Dict]`

=== "Example"

    ```python
    from quantel import Quantel

    qt = Quantel(api_key="<your-quantel-api-key>")

    goog = qt.ticker('goog')
    goog.income_statement_growth()
    ```

=== "Data"

    ```python
    [{'date': '2020-12-31',
     'growthCostAndExpenses': 0.10716468431197405,
     'growthCostOfRevenue': 0.17853566262378992,
     'growthDepreciationAndAmortization': 0.16263475087004498,
     'growthEBITDA': 0.19362340259062852,
     'growthEBITDARatio': 0.05845328676366234,
     'growthEPS': 0.18274129580595216,
     'growthEPSDiluted': 0.18274129580595216,
     'growthGeneralAndAdministrativeExpenses': 0.1571563187100827,
     'growthGrossProfit': 0.08708218005580196,
     'growthGrossProfitRatio': -0.03602283269164575,
     'growthIncomeBeforeTax': 0.21342586750788645,
     'growthIncomeBeforeTaxRatio': 0.07601325084630736,
     'growthIncomeTaxExpense': 0.4791745550927679,
     'growthInterestExpense': 0.35,
     'growthNetIncome': 0.1725533587630667,
     'growthNetIncomeRatio': 0.03976928886857504,
     'growthOperatingExpenses': 0.04697129531952696,
     'growthOperatingIncome': 0.20428851041453652,
     'growthOperatingIncomeRatio': 0.06791064023495606,
     'growthOtherExpenses': -1.2309974045235448,
     'growthResearchAndDevelopmentExpenses': 0.059766315627642404,
     'growthRevenue': 0.12770532012826136,
     'growthSellingAndMarketingExpenses': -0.028054592720970536,
     'growthTotalOtherIncomeExpensesNet': -65.9113924050633,
     'growthWeightedAverageShsOut': -0.02448500727940423,
     'growthWeightedAverageShsOutDil': -0.01695822341614936,
     'period': 'FY',
     'symbol': 'GOOG'},
    ...
    ```

### **cash_flow**

=== "Details"

    - *Description*:  Retrieves all cash flow statements
    - *Return*:  `List[Dict]`

=== "Example"

    ```python
    from quantel import Quantel

    qt = Quantel(api_key="<your-quantel-api-key>")

    goog = qt.ticker('goog')
    goog.cash_flow()
    ```

=== "Data"

    ```python
    [{'acceptedDate': '2021-02-02 20:12:25',
     'accountsPayables': 694000000,
     'accountsReceivables': -6524000000,
     'acquisitionsNet': -738000000,
     'capitalExpenditure': -22281000000,
     'cashAtBeginningOfPeriod': 18498000000,
     'cashAtEndOfPeriod': 26465000000,
     'changeInWorkingCapital': 1827000000,
     'commonStockIssued': 0,
     'commonStockRepurchased': -31149000000,
     'date': '2020-12-31',
     'debtRepayment': -2100000000,
     'deferredIncomeTax': 1390000000,
     'depreciationAndAmortization': 13697000000,
     'dividendsPaid': 0,
     'effectOfForexChangesOnCash': 24000000,
     'fillingDate': '2021-02-03',
     'freeCashFlow': 42843000000,
     'inventory': 0,
     'investmentsInPropertyPlantAndEquipment': -22281000000,
     'netCashProvidedByOperatingActivities': 65124000000,
     'netCashUsedForInvestingActivites': -32773000000,
     'netCashUsedProvidedByFinancingActivities': -24408000000,
     'netChangeInCash': 7967000000,
     'netIncome': 40269000000,
     'operatingCashFlow': 65124000000,
     'otherFinancingActivites': 2800000000,
     'otherInvestingActivites': 68000000,
     'otherNonCashItems': 1267000000,
     'otherWorkingCapital': 117462000000,
     'period': 'FY',
     'purchasesOfInvestments': -143751000000,
     'reportedCurrency': 'USD',
     'salesMaturitiesOfInvestments': 133929000000,
     'stockBasedCompensation': 12991000000,
     'symbol': 'GOOG'},
    ...
    ```

### **cash_flow_ttm**

=== "Details"

    - *Description*:  Retrieves cash flow statement trailing twelve months
    - *Return*:  `List[Dict]`

=== "Example"

    ```python
    from quantel import Quantel

    qt = Quantel(api_key="<your-quantel-api-key>")

    goog = qt.ticker('goog')
    goog.cash_flow_ttm()
    ```

=== "Data"

    ```python
    [{
        "symbol": "GOOG",
        "reportedCurrency": "USD",
        "period": "TTM",
        "netIncomeTTM": 62929000000,
        "depreciationAndAmortizationTTM": 12901000000,
        "deferredIncomeTaxTTM": 3285000000,
        "stockBasedCompensationTTM": 13966000000,
        "changeInWorkingCapitalTTM": 354000000,
        "accountsReceivablesTTM": -9913000000,
        "inventoryTTM": 0,
        "accountsPayablesTTM": 271000000,
        "otherWorkingCapitalTTM": 995000000,
        "otherNonCashItemsTTM": 335000000,
        "netCashProvidedByOperatingActivitiesTTM": 80859000000,
        "investmentsInPropertyPlantAndEquipmentTTM": -22323000000,
        "acquisitionsNetTTM": -2357000000,
        "purchasesOfInvestmentsTTM": -140350000000,
        "salesMaturitiesOfInvestmentsTTM": 128505000000,
        "otherInvestingActivitesTTM": -410000000,
        "netCashUsedForInvestingActivitesTTM": -36935000000,
        "debtRepaymentTTM": -8796000000,
        "commonStockIssuedTTM": 0,
        "commonStockRepurchasedTTM": -39992000000,
        "dividendsPaidTTM": 0,
        "otherFinancingActivitesTTM": 10467000000,
        "netCashUsedProvidedByFinancingActivitiesTTM": -38321000000,
        "effectOfForexChangesOnCashTTM": 285000000,
        "netChangeInCashTTM": 5888000000,
        "cashAtEndOfPeriodTTM": 96846000000,
        "cashAtBeginningOfPeriodTTM": 90958000000,
        "operatingCashFlowTTM": 80859000000,
        "capitalExpenditureTTM": -22323000000,
        "freeCashFlowTTM": 58536000000
    }]
    ...
    ```
    
   ### **cash_flow_growth**

=== "Details"

    - *Description*:  Retrieves cash flow statements growth by percentage data
    - *Return*:  `List[Dict]`

=== "Example"

    ```python
    from quantel import Quantel

    qt = Quantel(api_key="<your-quantel-api-key>")

    goog = qt.ticker('goog')
    goog.cash_flow_growth()
    ```

=== "Data"

    ```python
    [{'date': '2020-12-31',
     'growthAccountsPayables': 0.6214953271028038,
     'growthAccountsReceivables': 0.5032258064516129,
     'growthAcquisitionsNet': -0.7065606361829025,
     'growthCapitalExpenditure': -0.05380499405469679,
     'growthCashAtBeginningOfPeriod': 0.10759834740434704,
     'growthCashAtEndOfPeriod': 0.43069521029300467,
     'growthChangeInWorkingCapital': 1.2307692307692308,
     'growthCommonStockIssued': 0.0,
     'growthCommonStockRepurchased': 0.6932485322896281,
     'growthDebtRepayment': 2.58974358974359,
     'growthDeferredIncomeTax': 7.034682080924855,
     'growthDepreciationAndAmortization': 0.16263475087004498,
     'growthDividendsPaid': 0.0,
     'growthEffectOfForexChangesOnCash': -2.0434782608695654,
     'growthFreeCashFlow': 0.38328167376985667,
     'growthInventory': 0.0,
     'growthInvestmentsInPropertyPlantAndEquipment': -0.05380499405469679,
     'growthNetCashProvidedByOperatingActivites': 0.19449743213499635,
     'growthNetCashUsedForInvestingActivites': 0.11128818961717134,
     'growthNetCashUsedProvidedByFinancingActivities': 0.0516609935800767,
     'growthNetChangeInCash': 3.433500278241514,
     'growthNetIncome': 0.1725533587630667,
     'growthOperatingCashFlow': 0.19449743213499635,
     'growthOtherFinancingActivites': -1.6622516556291391,
     'growthOtherInvestingActivites': -0.9964182249144061,
     'growthOtherNonCashItems': -0.8288762830902215,
     'growthOtherWorkingCapital': 0.09412520841677767,
     'growthPurchasesOfInvestments': 0.19154032973317972,
     'growthSalesMaturitiesOfInvestments': 0.36342257965998165,
     'growthStockBasedCompensation': 0.2035390031498981,
     'period': 'FY',
     'symbol': 'GOOG'},
    ...
    ```
    
### **ratios**

=== "Details"

    - *Description*:  Retrieves all key financial ratios
    - *Return*:  `List[Dict]`

=== "Example"

    ```python
    from quantel import Quantel

    qt = Quantel(api_key="<your-quantel-api-key>")

    goog = qt.ticker('goog')
    goog.ratios()
    ```

=== "Data"

    ```python
    [{'assetTurnover': 0.57108217360833,
     'capitalExpenditureCoverageRatio': -2.9228490642251246,
     'cashConversionCycle': 41.81898753722751,
     'cashFlowCoverageRatios': None,
     'cashFlowToDebtRatio': 4.674418604651163,
     'cashPerShare': 202.33517174821117,
     'cashRatio': 0.4656543618256677,
     'companyEquityMultiplier': 1.4361923934143361,
     'currentRatio': 3.0667558151810534,
     'date': '2020-12-31',
     'daysOfInventoryOutstanding': 3.136005287258651,
     'daysOfPayablesOutstanding': 24.075732899022803,
     'daysOfSalesOutstanding': 62.758715148991655,
     'debtEquityRatio': 0.436192393414336,
     'debtRatio': 0.3037144573488186,
     'dividendPaidAndCapexCoverageRatio': None,
     'dividendPayoutRatio': None,
     'dividendYield': None,
     'ebitPerRevenue': 0.22585151785763202,
     'ebtPerEbit': 1.1663594022899282,
     'effectiveTaxRate': 0.16249324071378063,
     'enterpriseValueMultiple': 22.353196298759674,
     'fixedAssetTurnover': 1.8824979372937294,
     'freeCashFlowOperatingCashFlowRatio': 0.6578680670720471,
     'freeCashFlowPerShare': 63.41643205413999,
     'grossProfitMargin': 0.5357837470620785,
     'interestCoverage': 305.36296296296297,
     'inventoryTurnover': 116.39010989010988,
     'longTermDebtToCapitalization': 0.05891506960537222,
     'netIncomePerEBT': 0.8375067592862194,
     'netProfitMargin': 0.22061941520980458,
     'operatingCashFlowPerShare': 96.3968844640621,
     'operatingCashFlowSalesRatio': 0.35679105009121936,
     'operatingCycle': 65.89472043625031,
     'operatingProfitMargin': 0.22585151785763202,
     'payablesTurnover': 15.160493827160494,
     'payoutRatio': 0.0,
     'period': 'FY',
     'pretaxProfitMargin': 0.2634240413747007,
     'priceBookValueRatio': 5.572798610271138,
     'priceCashFlowRatio': 19.04356142012438,
     'priceEarningsRatio': 30.797707763395664,
     'priceEarningsToGrowthRatio': 1.6853173568441193,
     'priceFairValue': 5.572798610271138,
     'priceSalesRatio': 6.79457227656281,
     'priceToBookRatio': 5.572798610271138,
     'priceToFreeCashFlowsRatio': 28.94738682921784,
     'priceToOperatingCashFlowsRatio': 19.04356142012438,
     'priceToSalesRatio': 6.79457227656281,
     'quickRatio': 2.9573494739064645,
     'receivablesTurnover': 5.815925312261025,
     'returnOnAssets': 0.12599181517821387,
     'returnOnCapitalEmployed': 0.15687528065088172,
     'returnOnEquity': 0.18094848659141563,
     'shortTermCoverageRatios': None,
     'symbol': 'GOOG',
     'totalDebtToCapitalization': None},
    ...
    ```
    
### **historical_price**

=== "Details"

    - *Description*:  Retrieves historical price data
    - *Return*:  `List[Dict]`

=== "Example"

    ```python
    from quantel import Quantel

    qt = Quantel(api_key="<your-quantel-api-key>")

    goog = qt.ticker('goog')
    goog.historical_price()
    ```

=== "Data"

    ```python
      [
          {
              "symbol": "GOOG",
              "historical": [
                  {
                      "high": 2884.84,
                      "vwap": 2845.37,
                      "close": 2829.27,
                      "date": "2021-09-17",
                      "change": -46.7,
                      "open": 2875.97,
                      "changePercent": -1.624,
                      "adjClose": 2829.27,
                      "volume": 2603121,
                      "low": 2822.0
                  },
                  {
                      "high": 2904.0,
                      "vwap": 2887.04333,
                      "close": 2887.47,
                      "date": "2021-09-16",
                      "change": -14.95,
                      "open": 2902.42,
                      "changePercent": -0.515,
                      "adjClose": 2887.47,
                      "volume": 1025063,
                      "low": 2869.66
                  },
                  {
                      "high": 2911.63,
                      "vwap": 2887.04,
                      "close": 2904.12,
                      "date": "2021-09-15",
                      "change": 28.94,
                      "open": 2875.18,
                      "changePercent": 1.007,
                      "adjClose": 2904.12,
                      "volume": 1029778,
                      "low": 2845.37
                  },
                  {
                      "high": 2894.55,
                      "vwap": 2873.59333,
                      "close": 2868.12,
                      "date": "2021-09-14",
                      "change": -15.1,
                      "open": 2883.22,
                      "changePercent": -0.524,
                      "adjClose": 2868.12,
                      "volume": 936922,
                      "low": 2858.11
                  },
                  {
                      "high": 2883.0,
                      "vwap": 2865.98333,
                      "close": 2869.3,
                      "date": "2021-09-13",
                      "change": 5.28,
                      "open": 2864.02,
                      "changePercent": 0.184,
                      "adjClose": 2869.3,
                      "volume": 1009836,
                      "low": 2845.65
                  },
    ...
    ```

### **key_metrics**

=== "Details"

    - *Description*:  Retrieves all key financial metrics
    - *Return*:  `List[Dict]`

=== "Example"

    ```python
    from quantel import Quantel

    qt = Quantel(api_key="<your-quantel-api-key>")

    goog = qt.ticker('goog')
    goog.key_metrics()
    ```

=== "Data"

    ```python
    [{'averageInventory': 863500000.0,
     'averagePayables': 5575000000.0,
     'averageReceivables': 29438000000.0,
     'bookValuePerShare': 329.4107895118579,
     'capexPerShare': -32.98045240992211,
     'capexToDepreciation': -1.6267065780827918,
     'capexToOperatingCashFlow': -0.34213193292795285,
     'capexToRevenue': -0.12206961161910293,
     'cashPerShare': 202.33517174821117,
     'currentRatio': 3.0667558151810534,
     'date': '2020-12-31',
     'daysOfInventoryOnHand': 3.136005287258651,
     'daysPayablesOutstanding': 24.075732899022803,
     'daysSalesOutstanding': 62.758715148991655,
     'debtToAssets': 0.3037144573488186,
     'debtToEquity': 0.06260335034869509,
     'dividendYield': None,
     'earningsYield': 0.03246994898719511,
     'enterpriseValue': 1227659893924.18,
     'enterpriseValueOverEBITDA': 22.353196298759674,
     'evToFreeCashFlow': 28.654853626594306,
     'evToOperatingCashFlow': 18.851113167560037,
     'evToSales': 6.725908462442159,
     'freeCashFlowPerShare': 63.41643205413999,
     'freeCashFlowYield': 0.03454543257737714,
     'grahamNetNet': 94.02855611902034,
     'grahamNumber': 664.67073354722,
     'incomeQuality': 1.617224167473739,
     'intangiblesToTotalAssets': 0.07077242691229475,
     'interestCoverage': 305.36296296296297,
     'interestDebtPerShare': 20.822046768563993,
     'inventoryTurnover': 116.39010989010988,
     'investedCapital': 0.06260335034869509,
     'marketCap': 1240192893924.18,
     'netCurrentAssetValue': 77224000000.0,
     'netDebtToEBITDA': -0.2282005061816063,
     'netIncomePerShare': 59.60638382905406,
     'operatingCashFlowPerShare': 96.3968844640621,
     'payablesTurnover': 15.160493827160494,
     'payoutRatio': 0.0,
     'pbRatio': 5.572798610271138,
     'peRatio': 30.797707763395664,
     'period': 'FY',
     'pfcfRatio': 28.94738682921784,
     'pocfratio': 19.04356142012438,
     'priceToSalesRatio': 6.79457227656281,
     'ptbRatio': 5.572798610271138,
     'receivablesTurnover': 5.815925312261025,
     'researchAndDdevelopementToRevenue': 0.15106258252203783,
     'returnOnTangibleAssets': 0.135587684682622,
     'revenuePerShare': 270.17741739714796,
     'roe': 0.18094848659141563,
     'roic': 0.15687528065088172,
     'salesGeneralAndAdministrativeToRevenue': 0.060549946035381066,
     'shareholdersEquityPerShare': 329.4107895118579,
     'stockBasedCompensationToRevenue': 0.0711730319350014,
     'symbol': 'GOOG',
     'tangibleAssetValue': 199924000000.0,
     'tangibleBookValuePerShare': 295.9285475338301,
     'workingCapital': 117462000000.0},
    ...
    ```