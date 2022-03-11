
# EC2-Manager

Flask ve BOTO3 kütüphanelerini kullanarak AWS içerisinde:
- EC2 ID listeleme
- EC2 Instance çalıştırma
- EC2 Instance Durdurma

işlevlerini yapan API.



Kurulum yapmadan istek atmak için: http://ec2-3-120-129-120.eu-central-1.compute.amazonaws.com:3000/

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

```http
  POST ec2/list
```

| Parametre | Tip     | Açıklama                |
| :-------- | :------- | :------------------------- |
| `aws_access_key_id` | `string` | **Gerekli**. AWS Access anahtarınız. |
| `aws_secret_access_key` | `string` | **Gerekli**. AWS Secret Access anahtarınız. |
| `region_name` | `string` | **Gerekli** AWS EC2 bölgeniz |

#### AWS konsolunuz içerisinde ID'sini verdiğiniz Instance'ı çalıştırma

```http
  POST ec2/start
```

| Parametre | Tip     | Açıklama                |
| :-------- | :------- | :------------------------- |
| `aws_access_key_id` | `string` | **Gerekli**. AWS Access anahtarınız. |
| `aws_secret_access_key` | `string` | **Gerekli**. AWS Secret Access anahtarınız. |
| `region_name` | `string` | **Gerekli** AWS EC2 bölgeniz |
| `InstanceId` | `string` | **Gerekli** AWS EC2 Instance ID'si |
  
#### AWS konsolunuz içerisinde ID'sini verdiğiniz Instance'ı durdurma

```http
  POST ec2/stop
```

| Parametre | Tip     | Açıklama                |
| :-------- | :------- | :------------------------- |
| `aws_access_key_id` | `string` | **Gerekli**. AWS Access anahtarınız. |
| `aws_secret_access_key` | `string` | **Gerekli**. AWS Secret Access anahtarınız. |
| `region_name` | `string` | **Gerekli** AWS EC2 bölgeniz |
| `InstanceId` | `string` | **Gerekli** AWS EC2 Instance ID'si |
  


## Ekran Görüntüleri

![/](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ecbd2111-1965-4bd4-8988-abc57cafaedb/1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220310T204332Z&X-Amz-Expires=86400&X-Amz-Signature=b244e95248b89a951f91b29ae5ed5b2d8c5581daec1a1be08026feb1cf0da4cc&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%221.png%22&x-id=GetObject)

![/list](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/56d16545-55ec-472e-9b79-2fa017c6c21f/2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220310T204428Z&X-Amz-Expires=86400&X-Amz-Signature=d6a8925ce9c68c362ac4b6c7f9b0a9d9d0be0e5d4ffbeaa6b7e64b1abda41039&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%222.png%22&x-id=GetObject)  

![/start](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/e51adba3-c9a9-43b1-ba20-f8291ed22f2f/3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220310T204438Z&X-Amz-Expires=86400&X-Amz-Signature=5235bfc366fffaf32ae34c2d465b09f0cb3617af076a86890413308458724b1d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%223.png%22&x-id=GetObject)  

![/stop](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/6d0c80d2-1653-445b-b466-56532055702f/4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220310T204454Z&X-Amz-Expires=86400&X-Amz-Signature=d71981382729dc2c85ebf301c323f173643ab51a25162d8b378ec3b37cfea574&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%224.png%22&x-id=GetObject)  

![/error](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b739a004-cc6d-4972-ad5c-6b97bb32e88d/5.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220310T204504Z&X-Amz-Expires=86400&X-Amz-Signature=00e36edf6197f48c44d2f9a298b790f1d4ae0824478dd6c75c9fd3b9aa079b51&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%225.png%22&x-id=GetObject)  
