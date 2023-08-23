class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        return f"name: {self.name}  username: {self.username}"

    def create_member():
        cnt = 0
        print("멤버 인스턴스 생성 개수 입력")
        cnt_members = int(input("개수 : "))
        print("멤버 정보 작성")

        while True:
            if cnt == cnt_members:
                break
            else:
                cnt += 1
                print(f"{cnt}번째 멤버 정보 작성")
                name = input("Name: ")
                username = input("ID: ")
                password = input("PW: ")
                member = Member(name, username, password)
                members.append(member)


members = []
Member.create_member()


while len(members) < 3:
    print("3명 이상의 멤버를 생성하세요")
    Member.create_member()

for idx, member in enumerate(members):
    print(f"{idx + 1}번째 멤버{member.display()}")


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def create_post():
        cnt = 0
        print("게시물 생성 개수 입력")
        cnt_post = int(input("개수 : "))
        print("게시물 정보 작성")

        while True:
            if cnt == cnt_post:
                break
            else:
                cnt += 1
                print(f"{cnt}번째 게시물 정보 작성")
                title = input("Tit: ")
                content = input("Content: ")
                author = input("Author: ")
                post = Post(title, content, author)
                posts.append(post)


posts = []
Post.create_post()
print("게시물: ", posts)

# 1. **`Member`** 클래스와 **`Post`** 클래스를 정의하세요. ㅇ
# 2. **`Member`** 클래스에는 다음과 같은 속성을 가지고 있어야 합니다.
#     - 회원 이름 (**`name`**) ㅇ
#     - 회원 아이디 (**`username`**) ㅇ
#     - 회원 비밀번호 (**`password`**) ㅇ
# 3. **`Member`** 클래스에는 다음과 같은 메소드를 가지고 있어야 합니다.
#     - 회원 정보를 print해주는 `display` (회원이름과 아이디만 보여주고 비밀번호는 보여줘서는 안됩니다!) ㅇ
# 4. **`Post`** 클래스에는 다음과 같은 속성을 가지고 있어야 합니다.
#     - 게시물 제목 (**`title`**) ㅇ
#     - 게시물 내용 (**`content`**) ㅇ
#     - 작성자 (**`author`**) : 회원의 `username` 이 저장되어야 함! ㄴ
# 5. 회원 인스턴스를 세개 이상 만들고 `members` 라는 빈리스트에 append를 써서 저장해주세요 ㅇ
#     1. members 리스트를 돌면서 회원들의 이름을 모두 프린트 해주세요 ㅇ
# 6. 각각의 회원이 게시글을 세개 이상 작성하는 코드를 만들어주세요.(회원이 세명이명 총 9개 이상의 post 인스턴스가 만들어져야 합니다). 만들어진 게시글 인스턴스들은 posts 빈리스트에 append를 써서 저장해주세요 ㄴ
#     1. for 문을 돌면서 특정유저가 작성한 게시글의 제목을 모두 프린트 해주세요
#     2. for문을 돌면서 ‘특정 단어’가 content에 포함된 게시글의 제목을 모두 프린트 해주세요

# 1. input을 이용하여 Member 인스턴스 만드는것을 사용자가 터미널에서 할 수 있게 해주세요. ㅇ
# 2. post도 터미널에서 생성할 수 있게 해주세요. ㅇ
# 3. (심화)비밀번호 해싱이 무엇인지 공부한 후 hashlib 라이브러리를 써서 회원 비밀번호를 해시화하여 저장하게 해주세요. ㄴ

# **평가**

# - 클래스와 인스턴스 개념을 설명할 수 있는가?
# - 메소드와 어트리뷰트(속성)을 설명할 수 있는가?
# - 클래스를 정의할 수 있는가?
# - 인스턴스를 생성할 수 있는가?
