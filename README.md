# mail checker

주기적으로 메일 박스를 체크해서 변경 사항을 감지하여 슬랙에 알려줍니다

## Arguments

루트 폴더에 arguments.py 를 생성해야 합니다 arguments.py에는

USERS,
SLACK_TOKEN,
NOTI_ROOM

이 있어야 합니다

USERS는 리스트를 담는 리스트 객체입니다. 요소가 되는 리스트의 길이는 4이며 각각 메일 박스의 호스트, 유저네임, 비밀번호, 알려줄 슬랙 방 이름 이 됩니다

ex) [['mail.domain.com', 'personA@domain.com', 'password', '#noti-person-a'], ...]

SLACK_TOKEN 은 슬랙 토큰 값을 가지는 스트링입니다
NOTI_ROOM은 오류가 났을 때 알려줄 방 이름입니다
