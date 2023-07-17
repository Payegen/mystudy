
import requests

header = {
    # 'referer': 'https://www.jianshu.com/u/decb526c04b4',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}

# https://www.jianshu.com/asimov/users/slug/decb526c04b4/public_notes?page=1&count=10&order_by=shared_at

s = 'https://www.jianshu.com/asimov/p/'
for i in range(10):
    res = requests.get(
        'https://www.jianshu.com/asimov/users/slug/decb526c04b4/public_notes?page=1&count=10&order_by=shared_at',
        headers=header)

    if res.status_code == 200:
        result = res.json()
        title = result[i]['object']['data']['title']
        slug = result[i]['object']['data']['slug']
        # https://www.jianshu.com/asimov/p/49d18963a1c5
        new_url = s+ slug

        chapter = requests.get(new_url,headers=header).json()
        description = chapter['description']
        free_content = chapter['free_content']
        print(free_content)
        with open('demo{}.html'.format(i),'w',encoding='gbk') as f:
            f.write(free_content)
        # exit()







