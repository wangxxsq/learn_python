# encoding:utf8
# Python使用ORM框架操作数据库
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):

    """
    CREATE TABLE purus.operation_log (
      id       int             NOT NULL AUTO_INCREMENT,
      name    varchar(20)      NOT NULL,
      age     varchar(100)     NOT NULL,
      PRIMARY KEY (id)
    ) DEFAULT CHARSET=utf8;
    """
    __tablename__ = 'user'  # 表名

    id = Column(Integer, primary_key=True)  # 表结构
    name = Column(String)
    age = Column(String)


engine = create_engine('mysql+mysqlconnector://root:11111@localhost:3306/test')  # 初始化数据库连接:
DB_Session = sessionmaker(bind=engine)  # 创建DBSession类型:

# 增
session = DB_Session()  # 创建session对象:
user = User(id='1', name='xilming', age='18')  # 创建新User对象:
session.add(user)  # 添加到session:
session.commit()  # 提交即保存到数据库:
session.close()  # 关闭session:


# 查
session = DB_Session()
user_info = session.query(User).filter(User.id == '1').one()
print(user_info.name)
session.close()


# 改
session = DB_Session()
session.query(User).filter(User.id == '1').update({'name': 'xinxin'})
session.commit()
session.close()

# # 删
session = DB_Session()
session.query(User).filter(User.id == '1').delete()
session.commit()
session.close()







