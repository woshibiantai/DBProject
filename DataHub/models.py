from ModelClass import Model,Column

class users(Model):
    id = Column('id','int',unique=True)
    password = Column('password','char',not_null=True)
    email = Column('email','char',unique=True,not_null=True)
    display_name = Column('display_name','char', not_null=True)
    admin = Column('admin','int', not_null=True)

class dataset_list(Model):
    id = Column('id','int',unique=True)
    name = Column('name','char',not_null=True)
    creator_user_id = Column('creator_user_id','int',not_null=True)
    endorsed_by = Column('endorsed_by','char',not_null=True)

class user_dataset_following(Model):
    user_id = Column('user_id','int',not_null=True)
    dataset_id = Column('dataset_id','int',not_null=True)
    datetime_followed = Column('datetime_followed','datetime') # not_null=False as default=current_timestamp