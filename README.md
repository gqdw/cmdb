# cmdb

运行之前先配置accesskeyid，accesskeysecret

```
python ecs.py config --id=[accesskeyid] --secret=[accesskeysecret]
```

配置正确的话运行
 python ecs.py DescribeRegions 
会得到

```
{
  "Regions": {
    "Region": [
      {
        "LocalName": "\u6df1\u5733",
        "RegionId": "cn-shenzhen"
      },
      {
        "LocalName": "\u9752\u5c9b",
        "RegionId": "cn-qingdao"
      },
      {
        "LocalName": "\u5317\u4eac",
        "RegionId": "cn-beijing"
      },
      {
        "LocalName": "\u9999\u6e2f",
        "RegionId": "cn-hongkong"
      },
      {
        "LocalName": "\u676d\u5dde",
        "RegionId": "cn-hangzhou"
      },
      {
        "LocalName": "\u7f8e\u56fd\u7845\u8c37",
        "RegionId": "us-west-1"
      }
    ]
  },
  "RequestId": "8C3B760F-D126-413E-A67D-D3E81C3E1CBF"
}
```

之后我又重写了一个django的项目，不单是界面了，重写了很多代码。
