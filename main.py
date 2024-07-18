from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os
from dotenv import load_dotenv
from pathlib import Path
from oauth2client.service_account import ServiceAccountCredentials

my_dir = Path(__file__).parent

# # .envファイルの読み込み
load_dotenv()

def main():
    # Google Drive 認証
    gauth = GoogleAuth()
    scope = ["https://www.googleapis.com/auth/drive"]
    gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name(os.getenv('SECRETS_PATH'), scope)

    # 認証情報を保存するファイル名
    # credentials_file = os.getenv('SECRETS_PATH')
    
    # gauth.settings_file = os.getenv('YAML_PATH')
    
# #認証情報が存在しない場合は以下を実行する必要があります
    # gauth.LocalWebserverAuth()
    
    # # 認証情報を読み込みます
    # gauth.LoadCredentialsFile(credentials_file)
    # gauth.CommandLineAuth()
    # gauth.LocalWebserverAuth()
    # gauth.ServiceAuth()
    
    # if gauth.credentials is None:
    #      # 認証画面を表示します（ブラウザが開かれます）
    #      gauth.CommandLineAuth()
    # elif gauth.access_token_expired:
    # #     # アクセストークンが期限切れの場合、リフレッシュします
    #     gauth.Refresh()
    # else:
    # #     # 既存の認証情報を使用します
    #     gauth.Authorize()
    
    # # 認証情報を保存します
    # gauth.SaveCredentialsFile(credentials_file)
    
    drive = GoogleDrive(gauth)
    
    # 画像ファイルのアップロード
    f = drive.CreateFile({"parents":[{'id':os.getenv('PARENT_ID')}],\
        "id":os.getenv('CHILD_ID'),\
        "title": "test.jpg",\
        "mimeType": "image/jpeg"})

    f.SetContentFile(os.getenv('LAB_IMAGE_PATH'))
    f.Upload()

if __name__ == "__main__":
    main()
