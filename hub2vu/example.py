from dotenv import load_dotenv
import os

# .env 파일 로드 (같은 폴더에 있어야 함)
load_dotenv()

# 환경 변수 읽기
api_key = os.getenv("OPENAI_API_KEY")

# 출력
if api_key:
    print(f"My API Key is : {api_key}")
else:
    print("OPENAI_API_KEY가 설정되어 있지 않습니다.")
