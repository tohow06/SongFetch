# Song Fetch

使用kkbox的OpenAPI來獲取歌手最熱門的歌曲清單，並利用pytube下載youtube搜尋到的第一個影片的音檔

## Requirements

### Packages
```
pip install kkbox-developer-sdk
```
### KKBOX Client ID 及 Client Secret

1. 依照[官方教學](https://docs-zhtw.kkbox.codes/#overview--%E4%BB%8B%E7%B4%B9)取得Client ID及Client Secret
2. 創建`secret.json`並儲存Client ID及Client Secret，如下
```json
{
  "CLIENT_ID": "Your Client ID",
  "CLIENT_SECRET": "Your Client Secret"
}
```


## Usage

### 歌手的熱門歌曲
1. 將歌手名稱條列至`singers.txt`
2. 執行`python main.py`

### youtube 播放清單
1. 從播放清單的網址可以知道撥放清單的id，如下
`https://www.youtube.com/playlist?list=這裡就是id`
2. 執行下面指令
```
python download_playlist.py -i 貼上id
```