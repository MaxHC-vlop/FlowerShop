# FlowerShop

Website for the sale of flowers.

## How to install

- Сlone this repository:
```bash
git clone git@github.com:MaxHC-vlop/FlowerShop.git
```
- You must have python3.9 (or higher) installed.

- Create a virtual environment on directory project:
```bash
python3 -m venv env
 ```
- Start the virtual environment:
```bash
. env/bin/activate
```
- Then use pip to install dependencies:
```bash
pip install -r requirements.txt
```
- Create an `.env` file and populate it:

```bash
SECRET_KEY='' - default('empty')

DEBUG='' - default('True')

ALLOWED_HOSTS='' - default(['127.0.0.1', 'localhost'])
```
