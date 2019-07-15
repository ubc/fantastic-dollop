from fastapi import HTTPException
from starlette.status import HTTP_403_FORBIDDEN

from miracle import Acl

# A dynamic permissions system would take too long to do, so just going
# to statically define the permissions here. Note that admins are not
# handled here. Admins have access to everything, so we can just handle
# them during permission checking

## Constants
# roles, need to ensure these match names in the roles table
# changing these will require an alembic migration to match
INSTRUCTOR = 'Instructor'
TA = 'Teaching Assistant'
GUEST = 'Guest'

# resources
COURSE = 'Course'
USER = 'User'
EXAM = 'Exam'

# permissions
CREATE = 'create'
READ = 'read'
UPDATE = 'update'
DELETE = 'delete'

denied = HTTPException(status_code=HTTP_403_FORBIDDEN,
                       detail='Permission denied.')

acl = Acl()

acl.add_role(INSTRUCTOR)
acl.add_role(TA)
acl.add_role(GUEST)

# defining resources & their permissions
acl.add({
    COURSE: {CREATE, READ, UPDATE, DELETE},
    EXAM: {CREATE, READ, UPDATE, DELETE},
    USER: {CREATE, READ, UPDATE, DELETE}
})

# granting access to resources
acl.grants({
    INSTRUCTOR: {
        COURSE: [READ, UPDATE],
        EXAM: [CREATE, READ, UPDATE, DELETE],
        USER: [CREATE, READ]
    },
    TA: {
        COURSE: [READ],
        EXAM: [READ],
        USER: [READ]
    },
    GUEST: {
        COURSE: [READ]
    }
})
