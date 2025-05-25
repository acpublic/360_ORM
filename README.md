## ORM(Object-Relational Mapping)
### Python
- SQLAlchemy
- Django ORM

### Java
- Hibernate

### JavaScript
- Sequelize

### Ruby
- ActiveRecord

## Django ORM
- データ作成（レコード追加）
```python
new_book = Book(title="Python実践", author="佐藤", published_date="2024-01-01")
new_book.save()
```
- データ取得（全件）
```python
books_by_sato = Book.objects.filter(author="佐藤")
```
- データ取得（条件付き）
```python
books = Book.objects.all()
```
- データ更新
```python
book = Book.objects.get(id=1)
book.title = "改訂版 Python実践"
book.save()
```
- データ削除
```python
book = Book.objects.get(id=1)
book.delete()
```
