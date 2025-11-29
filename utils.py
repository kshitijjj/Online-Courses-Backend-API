from flask_jwt_extended import get_jwt
from functools import wraps
from flask_smorest import abort

def instructor_required(fn):
    @wraps(fn)
    def check_role(*args,**kwargs):
        role=get_jwt()
        if role['role']=="instructor":
            return fn(*args,**kwargs)
        else:
            abort(404,message="Access Denied")
    return check_role

def admin_required(fn):
    @wraps(fn)
    def check_admin(*args,**kwargs):
        is_admin=get_jwt()
        if is_admin['is_admin']==True:
            return fn(*args,**kwargs)
        else:
            abort(404,message="Access Denied")
    return check_admin