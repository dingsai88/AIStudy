import requests
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def search_by_time2():
    begin_time = "2016-01-01T00:00:00"
    end_time = "2016-01-01T23:59:59"
    req_str = "{\"Id\":\"65cd5a55-dc29-46ec-8f55-30aae4c183e9\",\"Name\":null,\"ContextType\":null,\"Type\":null,\"Title\":\"advanced_search\",\"RootElements\":[{\"Id\":\"SearchType\",\"Params\":{\"Type\":\"Interactions\"}},{\"Id\":\"InteractionTypes\",\"Params\":{\"Calls\":true,\"Emails\":true,\"Chats\":true}}],\"Sections\":[{\"Id\":\"DateRange\",\"Categories\":[{\"Id\":\"DateRange\",\"Elements\":[{\"Id\":\"DateRangeCalls\",\"Params\":{\"Type\":\"Between\",\"To\":\"2023-01-01T23:59:59\",\"From\":\"2023-01-01T12:00:00\"}}]}]},{\"Id\":\"CustomData\",\"Categories\":[{\"Id\":\"CustomData\",\"Elements\":[{\"Id\":\"SetCD\",\"Params\":{\"Value\":\"CDSet1\"}}]}]}]}"
    logger.info("请求data: %s", req_str)

    # 请替换VER_INT_URL为实际的URL前缀
    url = "http://yxrecordapp/Ultra/api/SearchServices/UserForm/65cd5a55-dc29-46ec-8f55-30aae4c183e9?_dc=1708940694056&type=Recent"
    logger.info("url: %s", url)

    # 请替换session为实际的Cookie值
    cookies = {'session': 'JSESSIONID=8LTkyWjVduyHCJHaokQDKwU8DlwguhP6t6rRBuCscp-ox6ShU5JK!-206973810; LANGUAGE_ID=zh_CN; ASP.NET_SessionId=jotn1zyggin3ybxoxmcb5yn4; Impact360AuthToken=qRdCd1TQeW; .ASPXAUTH=BB4F5DF78831350D3EB4D3738700CF950E84A69EABC9F3EC7EE8C933D76966DC69A1FDC22D209464E3E32D1F0BA4689C72B15B8BFEE57B701F75F75E71DFB8FDF3C7C40DA557C4558C8DE483A9B6F7F16B514ADF838FC5508066369A834300F7; USER_ID=yingkuigou'}

    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, headers=headers, cookies=cookies, data=req_str, timeout=10)
        response.raise_for_status()  # 如果响应状态码不是200，将抛出HTTPError异常

        res_str = response.text
        logger.info("post result %s", res_str)
        return res_str
    except requests.exceptions.HTTPError as errh:
        logger.error("Http Error: %s", errh)
    except requests.exceptions.ConnectionError as errc:
        logger.error("Error Connecting: %s", errc)
    except requests.exceptions.Timeout as errt:
        logger.error("Timeout Error: %s", errt)
    except requests.exceptions.RequestException as err:
        logger.error("OOps: Something Else: %s", err)

# 调用函数
result = search_by_time2()
print(result)