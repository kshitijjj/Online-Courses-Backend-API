from marshmallow import Schema,fields

class signupSchema(Schema):
    id=fields.Int(dump_only=True)
    username=fields.Str(required=True)
    email=fields.Str(required=True)
    password=fields.Str(required=True,load_only=True)
    role=fields.Str(required=True)
    created_at=fields.DateTime(dump_only=True)
    
class loginSchema(Schema):
    id=fields.Int(dump_only=True)
    email=fields.Str(required=True)
    password=fields.Str(load_only=True)

class responseSchema(Schema):
    message=fields.Str()
    token=fields.Str()

class courseSchema(Schema):
    id = fields.Int(dump_only=True)
    course_title = fields.Str(required=True)
    price = fields.Int(required=True)
    total_enrolled = fields.Int(required=True)
    reviews = fields.Int(required=True)
    total_lectures = fields.Int(required=True)
    level = fields.Str(required=True)
    subject = fields.Str(required=True)
    content_duration = fields.Float(required=True)

    course_by = fields.Int(dump_only=True)

class enrolledcourseSchema(Schema):
    id=fields.Int()

class enrolledSchema(Schema):
    id=fields.Int()
    user_id=fields.Int()
    course=fields.Nested(courseSchema)

class usercourseSchema(Schema):
    course=fields.Nested(courseSchema)