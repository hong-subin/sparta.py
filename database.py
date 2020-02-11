# 0. pymongo 라이브러리를 불러온다.
import pymongo

# 1. DB에 접속한다.
client = pymongo.MongoClient("localhost", 27017)

# 2. DB를 연다. (엑셀파일)
client.sparta

# 3. collection을 연다. (탭/시트)
users = client.sparta.users

# 4. 데이터를 처리한다.
# 4-1. 추가: Document를 추가한다. (한 줄을 추가한다.) : insert
# users.insert_one({'name': '수빈', 'gender': 'F'})
# users.insert_one({'name': '예나', 'gender': 'F'})


# 4-2. 변경: Update
users.update_one({'name': '수빈'}, {'$set': {'gender': 'M'}})

# 4-3. 삭제: Delete
users.delete_one({'name': '수빈'})

# 4-4. 읽기: find
all_user = list(users.find({'gender': 'F'}, {'_id': False}))
for user in all_user:
    print(user)