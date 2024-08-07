from sqlalchemy import Column, String, DateTime, func, Integer, Float  # Integer
from api.ext import db
class Traline(db.Model):
    # 指定本类映射到users表
    __tablename__ = 'traline'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 标题
    title = Column(String(20))
    # 标题
    sub_title = Column(String(20))
    # 开始时间
    start_time = Column(DateTime(), default=func.now())
    # 结束时间
    end_time = Column(DateTime(), default=func.now())
    # 搜索位置
    location = Column(String(20))
    # 描述
    describe = Column(String(100))
    # 用户创建时间
    created_at = Column(DateTime(), default=func.now())
    # 用户创建人id
    created_by = Column(Integer)
    # 状态 0=草稿，1=在线，2=下线
    status = Column(Integer, default=0)


class TralineInfo(db.Model):
    # 指定本类映射到traline_info表
    __tablename__ = 'traline_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 行程id
    traline_id = Column(Integer())
    # 出行时间
    traline_time = Column(DateTime(), default=func.now())
    # 主标题
    title = Column(String(100))
    # 副标题
    sub_title = Column(String(100))
    # 行程描述
    content = Column(String(1000))
    # 行程第几天
    day_number = Column(Integer())
    # 用户创建时间
    created_at = Column(DateTime(), default=func.now())
    # 用户创建人id
    created_by = Column(Integer)