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
# モデル定義
```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title
```

- データ追加
```python
new_book = Book(title='Django for Beginners', author='John Smith', published_date='2022-01-01')
new_book.save()
```
- データ取得（すべて）
```python
books = Book.objects.all()
```
- データ取得（条件付き）
```python
book = Book.objects.get(pk=1)
```
- データ更新
```python
book.title = 'Django for Experts'
book.save()
```
- データ削除
```python
book.delete()
```
