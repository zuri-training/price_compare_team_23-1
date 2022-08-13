def get_ali_express_product(product_name):
    _products = [
        {
            "name": "Original iPhone 13 Mini 13mini RAM 4GB ROM 128/256GB",
            "brand": "iPhone",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005004334408697.html?spm=a2g0o.productlist.0.0.940abd5fqtahQM&algo_pvid=7e6476da-496c-4861-9684-1aea6b1766d2&algo_exp_id=7e6476da-496c-4861-9684-1aea6b1766d2-3&pdp_ext_f=%7B%22sku_id%22%3A%2212000029242906736%22%7D&pdp_npi=2%40dis%21NGN%21360983.41%21288786.73%21%21%213961.2%21%21%402103255a16602497015482168e8659%2112000029242906736%21sea&curPageLogUid=Yj7kd6QTaAdI",
            "price": "₦288,786.73",
            "platform_name": "AliExpress",
        },
        {
            "name": "Apple iPhone 11 128GB",
            "brand": "iPhone",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005004609920887.html?spm=a2g0o.productlist.0.0.46d652d33dnMCe&algo_pvid=6f5a6fb8-8669-4cb6-ba4f-f2196303b59e&algo_exp_id=6f5a6fb8-8669-4cb6-ba4f-f2196303b59e-12&pdp_ext_f=%7B%22sku_id%22%3A%2212000029819430518%22%7D&pdp_npi=2%40dis%21NGN%21199519.67%2119951",
            "price": "₦199,519.67",
            "platform_name": "AliExpress",
        },
        {
            "name": "Apple iPhone 11 pro 64GB 256GB 512GB ROM",
            "brand": "iPhone",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005004316753915.html?spm=a2g0o.productlist.0.0.46d652d33dnMCe&algo_pvid=6f5a6fb8-8669-4cb6-ba4f-f2196303b59e&algo_exp_id=6f5a6fb8-8669-4cb6-ba4f-f2196303b59e-50&pdp_ext_f=%7B%22sku_id%22%3A%2212000028729983678%22%7D&pdp_npi=2%40dis%21NGN%21276898.95%21221517.49%21%21%21%21%21%402103255b16602500282787611e9c40%2112000028729983678%21sea&curPageLogUid=hmYJEsUjDW8M",
            "price": "₦221,517.49",
            "platform_name": "AliExpress",
        },
        {
            "name": "Samsung Galaxy S8+ Duos S8",
            "brand": "Samsung",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/32957132010.html?spm=a2g0o.productlist.0.0.6f6f7e72dNTnIb&algo_pvid=eec33e8b-f1b0-4c90-a003-a4bb6344283c&algo_exp_id=eec33e8b-f1b0-4c90-a003-a4bb6344283c-47&pdp_ext_f=%7B%22sku_id%22%3A%2266492944252%22%7D&pdp_npi=2%40dis%21NGN%21120048.94%21120048.94%21%21%215282.99%21%21%402101e9ce16602506257351189eb6a8%2166492944252%21sea&curPageLogUid=XObaEOmO269Q",
            "price": "₦120,048.94",
            "platform_name": "AliExpress",
        },
        {
            "name": "Samsung Galaxy S9+ Duos",
            "brand": "Samsung",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/4000876916748.html?spm=a2g0o.productlist.0.0.6f6f7e72dNTnIb&algo_pvid=eec33e8b-f1b0-4c90-a003-a4bb6344283c&algo_exp_id=eec33e8b-f1b0-4c90-a003-a4bb6344283c-46&pdp_ext_f=%7B%22sku_id%22%3A%2210000010202491181%22%7D&pdp_npi=2%40dis%21NGN%21140545.1%21112436.08%21%21%214404.58%21%21%402101e9ce16602506257351189eb6a8%2110000010202491181%21sea&curPageLogUid=oUhPcOmraFGM",
            "price": "₦112,436.08",
            "platform_name": "AliExpress",
        },
        {
            "name": "Samsung Galaxy A10 A105FN/DS Dual Sim",
            "brand": "Samsung",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005001610532145.html?spm=a2g0o.productlist.0.0.6f6f7e72dNTnIb&algo_pvid=eec33e8b-f1b0-4c90-a003-a4bb6344283c&algo_exp_id=eec33e8b-f1b0-4c90-a003-a4bb6344283c-50&pdp_ext_f=%7B%22sku_id%22%3A%2212000016802168698%22%7D&pdp_npi=2%40dis%21NGN%2169854.26%2154486.33%21%21%214404.58%21%21%402101e9ce16602506257351189eb6a8%2112000016802168698%21sea&curPageLogUid=ldzUbTCQTPs5",
            "price": "₦54,486.33",
            "platform_name": "AliExpress",
        },
        {
            "name": "Xiaomi Cellphone Redmi Note 8 Smartphone",
            "brand": "Xiaomi",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005004204510781.html?spm=a2g0o.productlist.0.0.6f6f7e72dFv6rF&algo_pvid=85dbe62e-804f-4eb7-a28a-090e28dd02a8&algo_exp_id=85dbe62e-804f-4eb7-a28a-090e28dd02a8-20&pdp_ext_f=%7B%22sku_id%22%3A%2212000028369971748%22%7D&pdp_npi=2%40dis%21NGN%2194579.33%2161475.93%21%21%21%21%21%402101e9d516602515489735275ed635%2112000028369971748%21sea&curPageLogUid=vtleocH8KGFC",
            "price": "₦61,475.93",
            "platform_name": "AliExpress",
        },
        {
            "name": "Macbook air 12 inch Intel Core M 256GB,Retina Ultra thin notebook",
            "brand": "Apple",
            "category": "laptop",
            "link": "https://www.aliexpress.com/item/1005003698504103.html?spm=a2g0o.productlist.0.0.53df4ef6dzZYqt&algo_pvid=5534ade4-356a-41b3-a2f1-51e52bd61c4e&algo_exp_id=5534ade4-356a-41b3-a2f1-51e52bd61c4e-5&pdp_ext_f=%7B%22sku_id%22%3A%2212000026848716233%22%7D&pdp_npi=2%40dis%21NGN%21372277.21%21349940.58%21%21%21%21%21%40210318c916602534508875410efd25%2112000026848716233%21sea&curPageLogUid=NIRKNOajOurw",
            "price": "₦349,940.58",
            "platform_name": "AliExpress",
        },
        {
            "name": "Original Samsung Galaxy S10e S10E 5.8'",
            "brand": "Samsung",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005004243664079.html?spm=a2g0o.productlist.0.0.6f6f7e72dFv6rF&algo_pvid=85dbe62e-804f-4eb7-a28a-090e28dd02a8&algo_exp_id=85dbe62e-804f-4eb7-a28a-090e28dd02a8-22&pdp_ext_f=%7B%22sku_id%22%3A%2212000028504125001%22%7D&pdp_npi=2%40dis%21NGN%21108102.61%2174589.29%21%21%213948.65%21%21%402101e9d516602515489735275ed635%2112000028504125001%21sea&curPageLogUid=6UYrWKWZmpz1",
            "price": "₦74,589.29",
            "platform_name": "AliExpress",
        },
        {
            "name": "Global Version Xiaomi Redmi Note 11",
            "brand": "Redmi",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005004320718834.html?spm=a2g0o.productlist.0.0.74b06e67hyThbf&algo_pvid=7e22b9c4-9b3e-4b67-b71b-4148289e7739&algo_exp_id=7e22b9c4-9b3e-4b67-b71b-4148289e7739-3&pdp_ext_f=%7B%22sku_id%22%3A%2212000029368480503%22%7D&pdp_npi=2%40dis%21NGN%21167897.02%21120885.52%21%21%21%21%21%402101e9ce16602518043593020eb6ae%2112000029368480503%21sea&curPageLogUid=e3lvjifJ4P8j",
            "price": "₦120,885.52",
            "platform_name": "AliExpress",
        },
        {
            "name": "Global ROM Xiaomi Redmi K40 Gaming Smartphone",
            "brand": "Xiaomi",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005003981523799.html?spm=a2g0o.productlist.0.0.74b06e67hyThbf&algo_pvid=7e22b9c4-9b3e-4b67-b71b-4148289e7739&algo_exp_id=7e22b9c4-9b3e-4b67-b71b-4148289e7739-6&pdp_ext_f=%7B%22sku_id%22%3A%2212000029402353760%22%7D&pdp_npi=2%40dis%21NGN%21150584.04%21135525.64%21%21%212932.21%21%21%402101e9ce16602518043593020eb6ae%2112000029402353760%21sea&curPageLogUid=tWsdqIELRMcN",
            "price": "₦135,525.64",
            "platform_name": "AliExpress",
        },
        {
            "name": "Xiaomi Cellphone Redmi Note 8 Smartphone",
            "brand": "Xiaomi",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005004204510781.html?spm=a2g0o.productlist.0.0.74b06e67hyThbf&algo_pvid=7e22b9c4-9b3e-4b67-b71b-4148289e7739&algo_exp_id=7e22b9c4-9b3e-4b67-b71b-4148289e7739-25&pdp_ext_f=%7B%22sku_id%22%3A%2212000028369971751%22%7D&pdp_npi=2%40dis%21NGN%2194579.33%2161475.93%21%21%21%21%21%402101e9ce16602518043593020eb6ae%2112000028369971751%21sea&curPageLogUid=K6MifH0ZlnfB",
            "price": "₦61,475.93",
            "platform_name": "AliExpress",
        },
        {
            "name": "Xiaomi-Smartphone Redmi 9A Global ROM 4GB of RAM 64GB ",
            "brand": "Xiaomi",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005003908122328.html?spm=a2g0o.productlist.0.0.74b06e67hyThbf&algo_pvid=7e22b9c4-9b3e-4b67-b71b-4148289e7739&algo_exp_id=7e22b9c4-9b3e-4b67-b71b-4148289e7739-51&pdp_ext_f=%7B%22sku_id%22%3A%2212000029480723370%22%7D&pdp_npi=2%40dis%21NGN%2188668.9%2144334.45%21%21%212731.43%21%21%402101e9ce16602518043593020eb6ae%2112000029480723370%21sea&curPageLogUid=N0SMSj4pN9I1",
            "price": "₦44,334.45",
            "platform_name": "AliExpress",
        },
        {
            "name": "Xiaomi Redmi Note 11E 4GB/6GB 128GB Smartphones",
            "brand": "Xiaomi",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005004198516276.html?spm=a2g0o.productlist.0.0.74b06e67hyThbf&algo_pvid=7e22b9c4-9b3e-4b67-b71b-4148289e7739&algo_exp_id=7e22b9c4-9b3e-4b67-b71b-4148289e7739-28&pdp_ext_f=%7B%22sku_id%22%3A%2212000029036405459%22%7D&pdp_npi=2%40dis%21NGN%21121295.44%2160647.72%21%21%212731.43%21%21%402101e9ce16602518043593020eb6ae%2112000029036405459%21sea&curPageLogUid=z1yxKezkl16A",
            "price": "₦60,647.72",
            "platform_name": "AliExpress",
        },
        {
            "name": "Global Version Xiaomi Redmi Note 11 64GB / 128GB Smartphone",
            "brand": "Xiaomi",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005003847303397.html?spm=a2g0o.productlist.0.0.74b06e67hyThbf&algo_pvid=7e22b9c4-9b3e-4b67-b71b-4148289e7739&algo_exp_id=7e22b9c4-9b3e-4b67-b71b-4148289e7739-29&pdp_ext_f=%7B%22sku_id%22%3A%2212000029623911758%22%7D&pdp_npi=2%40dis%21NGN%2196566.2%2178220.04%21%21%21439.2%21%21%402101e9ce16602518043593020eb6ae%2112000029623911758%21sea&curPageLogUid=8mxhRnBWyrAW",
            "price": "₦78,220.04",
            "platform_name": "AliExpress",
        },
        {
            "name": "Infinix HOT 11S 6GB 128GB Smartphone",
            "brand": "Infinix",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005002722004135.html?spm=a2g0o.productlist.0.0.aaf959e8P3P6gM&algo_pvid=0479f5cc-5f6f-476d-a706-d4e9b10b77e7&algo_exp_id=0479f5cc-5f6f-476d-a706-d4e9b10b77e7-2&pdp_ext_f=%7B%22sku_id%22%3A%2212000029887315630%22%7D&pdp_npi=2%40dis%21NGN%2192019.4%2165332.56%21%21%218365.78%21%21%402101e9d516602525465682443ed63d%2112000029887315630%21sea&curPageLogUid=9Dpdepv6sxHV",
            "price": "₦65,332.56",
            "platform_name": "AliExpress",
        },
        {
            "name": "Infinix Hot 11 Play Global Version 6.82'' HD+ Display Smartphone",
            "brand": "Infinix",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005003509532336.html?spm=a2g0o.productlist.0.0.aaf959e8P3P6gM&algo_pvid=0479f5cc-5f6f-476d-a706-d4e9b10b77e7&algo_exp_id=0479f5cc-5f6f-476d-a706-d4e9b10b77e7-5&pdp_ext_f=%7B%22sku_id%22%3A%2212000029347563341%22%7D&pdp_npi=2%40dis%21NGN%2162220.49%2149776.39%21%21%218365.78%21%21%402101e9d516602525465682443ed63d%2112000029347563341%21sea&curPageLogUid=TbJQZHqjhQEY",
            "price": "₦49,776.39",
            "platform_name": "AliExpress",
        },
        {
            "name": "Infinix Note 11 Pro 8GB 128GB 6.95'' Display Smartphone",
            "brand": "Infinix",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005003407530072.html?spm=a2g0o.productlist.0.0.aaf959e8P3P6gM&algo_pvid=0479f5cc-5f6f-476d-a706-d4e9b10b77e7&algo_exp_id=0479f5cc-5f6f-476d-a706-d4e9b10b77e7-8&pdp_ext_f=%7B%22sku_id%22%3A%2212000029887048666%22%7D&pdp_npi=2%40dis%21NGN%21124888.55%2188668.9%21%21%219687.57%21%21%402101e9d516602525465682443ed63d%2112000029887048666%21sea&curPageLogUid=nRFvMbsxXaNK",
            "price": "₦88,668.90",
            "platform_name": "AliExpress",
        },
        {
            "name": "Global Version Infinix Note 10 Pro 2022 8GB+128GB Smartphone",
            "brand": "Infinix",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005004308954495.html?spm=a2g0o.productlist.0.0.aaf959e8P3P6gM&algo_pvid=0479f5cc-5f6f-476d-a706-d4e9b10b77e7&algo_exp_id=0479f5cc-5f6f-476d-a706-d4e9b10b77e7-23&pdp_ext_f=%7B%22sku_id%22%3A%2212000029519071467%22%7D&pdp_npi=2%40dis%21NGN%21116556.23%2188581.06%21%21%211761.0%21%21%402101e9d516602525465682443ed63d%2112000029519071467%21sea&curPageLogUid=9BB8E0uCGAd3",
            "price": "₦88,581.06 - ₦89,852.66",
            "platform_name": "AliExpress",
        },
        {
            "name": "Global Version Infinix HOT 11S NFC 4GB 64GB 6.78' FHD Punching Display 5000mAh Battery Smartphone",
            "brand": "Infinix",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005003534050694.html?spm=a2g0o.productlist.0.0.aaf959e8P3P6gM&algo_pvid=0479f5cc-5f6f-476d-a706-d4e9b10b77e7&algo_exp_id=0479f5cc-5f6f-476d-a706-d4e9b10b77e7-25&pdp_ext_f=%7B%22sku_id%22%3A%2212000027994634606%22%7D&pdp_npi=2%40dis%21NGN%2177906.33%2162325.06%21%21%215994.08%21%21%402101e9d516602525465682443ed63d%2112000027994634606%21sea&curPageLogUid=m65BNrF6N4Wf",
            "price": "₦62,325.06",
            "platform_name": "AliExpress",
        },
        {
            "name": "Macbook air laptop is ultra-thin, 256GB",
            "brand": "Apple",
            "category": "laptop",
            "link": "https://www.aliexpress.com/item/1005003412618918.html?spm=a2g0o.productlist.0.0.53df4ef6dzZYqt&algo_pvid=5534ade4-356a-41b3-a2f1-51e52bd61c4e&algo_exp_id=5534ade4-356a-41b3-a2f1-51e52bd61c4e-0&pdp_ext_f=%7B%22sku_id%22%3A%2212000025672752870%22%7D&pdp_npi=2%40dis%21NGN%21248463.67%21233555.85%21%21%21%21%21%40210318c916602534508875410efd25%2112000025672752870%21sea&curPageLogUid=BzYch4QOpNmb",
            "price": "₦33,555.85",
            "platform_name": "AliExpress",
        },
        {
            "name": "Macbook air 12 inch Intel Core M 512GB,Retina Ultra thin notebook",
            "brand": "Apple",
            "category": "laptop",
            "link": "https://www.aliexpress.com/item/1005004496055554.html?spm=a2g0o.productlist.0.0.53df4ef6dzZYqt&algo_pvid=5534ade4-356a-41b3-a2f1-51e52bd61c4e&algo_exp_id=5534ade4-356a-41b3-a2f1-51e52bd61c4e-2&pdp_ext_f=%7B%22sku_id%22%3A%2212000029361741198%22%7D&pdp_npi=2%40dis%21NGN%21414106.11%21393400.8%21%21%21%21%21%40210318c916602534508875410efd25%2112000029361741198%21sea&curPageLogUid=9xG1bY39AweC",
            "price": "₦393,400.80",
            "platform_name": "AliExpress",
        },
        {
            "name": "MacBook Pro 13.3 inch",
            "brand": "Apple",
            "category": "laptop",
            "link": "https://www.aliexpress.com/item/1005003968535232.html?spm=a2g0o.productlist.0.0.53df4ef6dzZYqt&algo_pvid=5534ade4-356a-41b3-a2f1-51e52bd61c4e&algo_exp_id=5534ade4-356a-41b3-a2f1-51e52bd61c4e-18&pdp_ext_f=%7B%22sku_id%22%3A%2212000027593256689%22%7D&pdp_npi=2%40dis%21NGN%21899321.35%21854355.28%21%21%21%21%21%40210318c916602534508875410efd25%2112000027593256689%21sea&curPageLogUid=GCzfHyaMbJk5",
            "price": "₦854,355.28",
            "platform_name": "AliExpress",
        },
        {
            "name": "Notebook 15.6 inch Laptop Windows 11",
            "brand": "Windows",
            "category": "laptop",
            "link": "https://www.aliexpress.com/item/1005004603775047.html?spm=a2g0o.productlist.0.0.6cf260f54vqdhs&algo_pvid=d8a7b829-b7ee-432a-9a3c-d8be06b83728&algo_exp_id=d8a7b829-b7ee-432a-9a3c-d8be06b83728-2&pdp_ext_f=%7B%22sku_id%22%3A%2212000029795685380%22%7D&pdp_npi=2%40dis%21NGN%21104526.24%21104526.24%21%21%2115409.77%21%21%402103143616602539516061390e509a%2112000029795685380%21sea&curPageLogUid=NsMe9aXe7ahl",
            "price": "₦104,526.24",
            "platform_name": "AliExpress",
        },
        {
            "name": "Computer 15.6 Inch Gaming Laptop Intel J3455 1920*1080 FHD IPS 8GB RAM 512G SSD Windows 10 ",
            "brand": "Windows",
            "category": "laptop",
            "link": "https://www.aliexpress.com/item/1005004137475940.html?spm=a2g0o.productlist.0.0.6cf260f54vqdhs&algo_pvid=d8a7b829-b7ee-432a-9a3c-d8be06b83728&algo_exp_id=d8a7b829-b7ee-432a-9a3c-d8be06b83728-8&pdp_ext_f=%7B%22sku_id%22%3A%2212000028305919519%22%7D&pdp_npi=2%40dis%21NGN%21202870.16%21101435.08%21%21%2119312.4%21%21%402103143616602539516061390e509a%2112000028305919519%21sea&curPageLogUid=vNsrpV3afy4g",
            "price": "₦101,435.08",
            "platform_name": "AliExpress",
        },
        {
            "name": "Dere V9 MAX Laptop 15.6'",
            "brand": "Windows",
            "category": "laptop",
            "link": "https://www.aliexpress.com/item/1005004383127851.html?spm=a2g0o.productlist.0.0.6cf260f54vqdhs&algo_pvid=d8a7b829-b7ee-432a-9a3c-d8be06b83728&aem_p4p_detail=202208111439114759416391265200004266713&algo_exp_id=d8a7b829-b7ee-432a-9a3c-d8be06b83728-19&pdp_ext_f=%7B%22sku_id%22%3A%2212000029783568445%22%7D&pdp_npi=2%40dis%21NGN%21290618.83%21247024.75%21%21%2144050.01%21%21%402103143616602539516061390e509a%2112000029783568445%21sea&curPageLogUid=lWXYoqQjQVRJ",
            "price": "₦247,024.75",
            "platform_name": "AliExpress",
        },
        {
            "name": "2022 Office Notebook Windows 11 Business Gaming Education Laptop ",
            "brand": "Windows",
            "category": "laptop",
            "link": "https://www.aliexpress.com/item/1005004622282764.html?spm=a2g0o.productlist.0.0.6cf260f54vqdhs&algo_pvid=d8a7b829-b7ee-432a-9a3c-d8be06b83728&algo_exp_id=d8a7b829-b7ee-432a-9a3c-d8be06b83728-18&pdp_ext_f=%7B%22sku_id%22%3A%2212000029866581614%22%7D&pdp_npi=2%40dis%21NGN%21125444.87%21119170.54%21%21%2127703.28%21%21%402103143616602539516061390e509a%2112000029866581614%21sea&curPageLogUid=FM6Y04Jz1350",
            "price": "₦119,170.54",
            "platform_name": "AliExpress",
        },
        {
            "name": "Lenovo V15 G2 Intel Core i5 1135 G7 8GB RAM 256GB SSD Windows 10 ",
            "brand": "Lenovo",
            "category": "laptop",
            "link": "https://www.aliexpress.com/item/1005004485324523.html?spm=a2g0o.productlist.0.0.6cf260f54vqdhs&algo_pvid=d8a7b829-b7ee-432a-9a3c-d8be06b83728&algo_exp_id=d8a7b829-b7ee-432a-9a3c-d8be06b83728-20&pdp_ext_f=%7B%22sku_id%22%3A%2212000029325968129%22%7D&pdp_npi=2%40dis%21NGN%21497763.91%21460076.07%21%21%21%21%21%402103143616602539516061390e509a%2112000029325968129%21sea&curPageLogUid=D1Oqdu5jCPR8",
            "price": "₦460,076.07",
            "platform_name": "AliExpress",
        },
        {
            "name": "Senior Laptop Lenovo ThinkBook 14",
            "brand": "Lenovo",
            "category": "laptop",
            "link": "https://www.aliexpress.com/item/1005001527379530.html?spm=a2g0o.productlist.0.0.29291068rEY6TW&algo_pvid=a05634d7-4302-40b7-a33a-54f1eb705b83&algo_exp_id=a05634d7-4302-40b7-a33a-54f1eb705b83-6&pdp_ext_f=%7B%22sku_id%22%3A%2212000027486329312%22%7D&pdp_npi=2%40dis%21NGN%21510312.58%21357218.81%21%21%21%21%21%402101e9cf16602544910904642e028c%2112000027486329312%21sea&curPageLogUid=pIWlxKx4Be1v",
            "price": "₦357,218.81",
            "platform_name": "AliExpress",
        },
        {
            "name": "Intel laptop 15.6 inch Windows 10",
            "brand": "Intel",
            "category": "laptop",
            "link": "https://www.aliexpress.com/item/4001151183493.html?spm=a2g0o.productlist.0.0.29291068rEY6TW&algo_pvid=a05634d7-4302-40b7-a33a-54f1eb705b83&algo_exp_id=a05634d7-4302-40b7-a33a-54f1eb705b83-25&pdp_ext_f=%7B%22sku_id%22%3A%2212000022130661127%22%7D&pdp_npi=2%40dis%21NGN%21137194.61%21100150.94%21%21%2141389.7%21%21%402101e9cf16602544910904642e028c%2112000022130661127%21sea&curPageLogUid=8cASexcBfc7i",
            "price": "₦100,150.94",
            "platform_name": "AliExpress",
        },
        {
            "name": "Original Apple iPhone XR",
            "brand": "iPhone",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005002294973714.html?spm=a2g0o.productlist.0.0.7ac866eb4may4b&algo_pvid=0e47f4fe-f494-4841-b3d6-9d0b9f7039d1&algo_exp_id=0e47f4fe-f494-4841-b3d6-9d0b9f7039d1-2&pdp_ext_f=%7B%22sku_id%22%3A%2212000019958696879%22%7D&pdp_npi=2%40dis%21NGN%21196160.81%21129464.63%21%21%21%21%21%40210318d116602554533612571e9f71%2112000019958696879%21sea&curPageLogUid=9rS1QL5cHnyp",
            "price": "₦129,464.63",
            "platform_name": "AliExpress",
        },
        {
            "name": "Original Apple iPhone XR",
            "brand": "iPhone",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005002211959517.html?spm=a2g0o.productlist.0.0.7ac866eb4may4b&algo_pvid=0e47f4fe-f494-4841-b3d6-9d0b9f7039d1&algo_exp_id=0e47f4fe-f494-4841-b3d6-9d0b9f7039d1-5&pdp_ext_f=%7B%22sku_id%22%3A%2212000029818836506%22%7D&pdp_npi=2%40dis%21NGN%21191718.58%21124616.66%21%21%21%21%21%40210318d116602554533612571e9f71%2112000029818836506%21sea&curPageLogUid=AEqUzGkJ1S0g",
            "price": "₦124,616.66",
            "platform_name": "AliExpress",
        },
        {
            "name": "Unlocked Original Apple iPhone XR",
            "brand": "iPhone",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005003624973744.html?spm=a2g0o.productlist.0.0.7ac866eb4may4b&algo_pvid=0e47f4fe-f494-4841-b3d6-9d0b9f7039d1&algo_exp_id=0e47f4fe-f494-4841-b3d6-9d0b9f7039d1-8&pdp_ext_f=%7B%22sku_id%22%3A%2212000026547539142%22%7D&pdp_npi=2%40dis%21NGN%21151629.76%21121303.81%21%21%212200.2%21%21%40210318d116602554533612571e9f71%2112000026547539142%21sea&curPageLogUid=QWUTD6Yifptq",
            "price": "₦121,303.81",
            "platform_name": "AliExpress",
        },
        {
            "name": "Samsung Galaxy S22 Ultra",
            "brand": "Samsung",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005004329502686.html?spm=a2g0o.productlist.0.0.3dc47ec6Lva6HM&algo_pvid=181b21e2-6190-4cdf-9fbe-363b25120ab9&algo_exp_id=181b21e2-6190-4cdf-9fbe-363b25120ab9-7&pdp_ext_f=%7B%22sku_id%22%3A%2212000028777509760%22%7D&pdp_npi=2%40dis%21NGN%21506129.69%21506129.69%21%21%215282.99%21%21%40210318b916602556850996952e1514%2112000028777509760%21sea&curPageLogUid=6bKt2RdHbWld",
            "price": "₦506,129.69",
            "platform_name": "AliExpress",
        },
        {
            "name": "Samsung Galaxy S22 Ultra",
            "brand": "Samsung",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005004571274864.html?spm=a2g0o.productlist.0.0.3dc47ec6Lva6HM&algo_pvid=181b21e2-6190-4cdf-9fbe-363b25120ab9&algo_exp_id=181b21e2-6190-4cdf-9fbe-363b25120ab9-0&pdp_ext_f=%7B%22sku_id%22%3A%2212000029670355733%22%7D&pdp_npi=2%40dis%21NGN%21542102.54%21433682.04%21%21%213961.2%21%21%40210318b916602556850996952e1514%2112000029670355733%21sea&curPageLogUid=XcNEh97Q5Hzs",
            "price": "₦433,682.04",
            "platform_name": "AliExpress",
        },
        {
            "name": "Samsung Galaxy S22 Ultra",
            "brand": "Samsung",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005004318748293.html?spm=a2g0o.productlist.0.0.3dc47ec6Lva6HM&algo_pvid=181b21e2-6190-4cdf-9fbe-363b25120ab9&algo_exp_id=181b21e2-6190-4cdf-9fbe-363b25120ab9-2&pdp_ext_f=%7B%22sku_id%22%3A%2212000028736101893%22%7D&pdp_npi=2%40dis%21NGN%21509894.29%21407915.43%21%21%213961.2%21%21%40210318b916602556850996952e1514%2112000028736101893%21sea&curPageLogUid=kyHWwGvZBNIp",
            "price": "₦407,915.43",
            "platform_name": "AliExpress",
        },
        {
            "name": "Genuine Apple iPhone X",
            "brand": "iPhone",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005003534400749.html?spm=a2g0o.productlist.0.0.6fcb10c5sLsenK&algo_pvid=9ff50c6b-6b92-427f-bc46-ceb2ffe463a2&algo_exp_id=9ff50c6b-6b92-427f-bc46-ceb2ffe463a2-10&pdp_ext_f=%7B%22sku_id%22%3A%2212000026204275779%22%7D&pdp_npi=2%40dis%21NGN%21143054.84%21114443.87%21%21%214404.58%21%21%402103255a16602549139266124e863e%2112000026204275779%21sea&curPageLogUid=Lvn4Evuiwgws",
            "price": "₦114,443.87",
            "platform_name": "AliExpress",
        },
        {
            "name": "Unlocked Apple iPhone X Hexa Core 3GB RAM Moible Phone",
            "brand": "iPhone",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/4000158856485.html?spm=a2g0o.productlist.0.0.6fcb10c5sLsenK&algo_pvid=9ff50c6b-6b92-427f-bc46-ceb2ffe463a2&algo_exp_id=9ff50c6b-6b92-427f-bc46-ceb2ffe463a2-6&pdp_ext_f=%7B%22sku_id%22%3A%2212000028112532394%22%7D&pdp_npi=2%40dis%21NGN%21221693.17%21110846.58%21%21%216604.78%21%21%402103255a16602549139266124e863e%2112000028112532394%21sea&curPageLogUid=EK45b5N6aXRJ",
            "price": "₦110,846.58",
            "platform_name": "AliExpress",
        },
        {
            "name": "Original Unlock Apple iPhone X",
            "brand": "iPhone",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005002488860142.html?spm=a2g0o.productlist.0.0.6fcb10c5sLsenK&algo_pvid=9ff50c6b-6b92-427f-bc46-ceb2ffe463a2&algo_exp_id=9ff50c6b-6b92-427f-bc46-ceb2ffe463a2-1&pdp_ext_f=%7B%22sku_id%22%3A%2212000020841095172%22%7D&pdp_npi=2%40dis%21NGN%21176994.81%21111507.48%21%21%21%21%21%402103255a16602549139266124e863e%2112000020841095172%21sea&curPageLogUid=3hexaJtsotSg",
            "price": "₦111,507.48",
            "platform_name": "AliExpress",
        },
        {
            "name": "Original Unlocked Cell phone Apple iPhone X",
            "brand": "iPhone",
            "category": "smartphones",
            "link": "https://www.aliexpress.com/item/1005003996185468.html?spm=a2g0o.productlist.0.0.6fcb10c5sLsenK&algo_pvid=9ff50c6b-6b92-427f-bc46-ceb2ffe463a2&algo_exp_id=9ff50c6b-6b92-427f-bc46-ceb2ffe463a2-0&pdp_ext_f=%7B%22sku_id%22%3A%2212000027684044321%22%7D&pdp_npi=2%40dis%21NGN%21123813.54%21111432.19%21%21%214404.58%21%21%402103255a16602549139266124e863e%2112000027684044321%21sea&curPageLogUid=Q4UlUcLkJMHx",
            "price": "₦111,432.19",
            "platform_name": "AliExpress",
        },
    ]

    for product in _products:
        if product["name"] in product_name:
            return product
