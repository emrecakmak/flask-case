
# EC2-Manager

Flask ve BOTO3 kütüphanelerini kullanarak AWS içerisinde:
- EC2 ID listeleme
- EC2 Instance çalıştırma
- EC2 Instance Durdurma

işlevlerini yapan API.



Kurulum yapmadan istek atmak için: http://ec2-35-157-122-137.eu-central-1.compute.amazonaws.com:3000/

## Bilgisayarınızda Çalıştırın

Projeyi klonlayın

```bash
  git clone https://github.com/emrecakmak/flask-case
```

Proje dizinine gidin

```bash
  cd flask-case
```

Docker build alın

```bash
  docker build -t flask-case:latest .
```

Docker containarı ayağa kaldıralım

```bash
  docker run -d -p 3000:3000 flask-case
```



  
## API Kullanımı

#### AWS konsolunuz içerisinde varolan tüm EC2 Instance ID'lerini getirme

```https
  POST ec2/list
```

| Parametre | Tip     | Açıklama                |
| :-------- | :------- | :------------------------- |
| `aws_access_key_id` | `string` | **Gerekli**. AWS Access anahtarınız. |
| `aws_secret_access_key` | `string` | **Gerekli**. AWS Secret Access anahtarınız. |
| `region_name` | `string` | **Gerekli** AWS EC2 bölgeniz |

#### AWS konsolunuz içerisinde ID'sini verdiğiniz Instance'ı çalıştırma

```https
  POST ec2/start
```

| Parametre | Tip     | Açıklama                |
| :-------- | :------- | :------------------------- |
| `aws_access_key_id` | `string` | **Gerekli**. AWS Access anahtarınız. |
| `aws_secret_access_key` | `string` | **Gerekli**. AWS Secret Access anahtarınız. |
| `region_name` | `string` | **Gerekli** AWS EC2 bölgeniz |
| `InstanceId` | `string` | **Gerekli** AWS EC2 Instance ID'si |
  
#### AWS konsolunuz içerisinde ID'sini verdiğiniz Instance'ı durdurma

```https
  POST ec2/stop
```

| Parametre | Tip     | Açıklama                |
| :-------- | :------- | :------------------------- |
| `aws_access_key_id` | `string` | **Gerekli**. AWS Access anahtarınız. |
| `aws_secret_access_key` | `string` | **Gerekli**. AWS Secret Access anahtarınız. |
| `region_name` | `string` | **Gerekli** AWS EC2 bölgeniz |
| `InstanceId` | `string` | **Gerekli** AWS EC2 Instance ID'si |
  


## Ekran Görüntüleri

![/](https://i.imgur.com/SHk3yWQ.png)

![/list](https://i.imgur.com/vaaM9tA.png)  

![/start](https://i.imgur.com/TPvqciu.png)  

![/stop](https://i.imgur.com/3naiTNL.png)  

![/error](https://i.imgur.com/WhqBn0q.png)  
