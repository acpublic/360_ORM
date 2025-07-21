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

## SQLAlchemy
- モデル定義
```python
class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    age = Column(Integer)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
```
- DB作成
```python
engine = create_engine('sqlite:///test.db', echo=True)

Base.metadata.create_all(engine)
```
- DB接続
```python
SessionClass = sessionmaker(engine)
session = SessionClass()
```
- INSERT
```python
user_i = User(first_name="first_a", last_name="last_a", age=20)
session.add(user_i)
session.commit()
```
- UPDATE
```python
user_u = session.query(User).get(min_id)
user_u.age = 10
session.commit()
```
- DELETE
```python
user_d = session.query(User).get(min_id)
session.delete(user_d)
session.commit()
```
- CLOSE
```python
session.close()
```

## Django ORM
- モデル定義
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
- フィルタリング
```python
books = Book.objects.filter(author__name='John Smith')
```
- ソート（昇順）
```python
books = Book.objects.order_by('published_date')
```
- ソート（降順）
```python
books = Book.objects.order_by('-published_date')
```
