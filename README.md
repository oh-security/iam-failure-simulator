# IAM Failure Simulator

This is a minimal README to verify Markdown rendering.

## Sample output

```json
{
  "ok": true
}
Intended audience
This text must be normal (not inside a code block).

yaml
コードをコピーする

---

## 3) Commit changes
Commitメッセージは適当でOK（例：`Reset README`）。

---

# ✅ 成功判定（これだけ見る）
README表示で：

- `Sample output` の **JSON部分だけ**が灰色のコードブロック
- `## Intended audience` とその文章が **普通の表示**

なら成功です。

---

# ここでまだダメなら「原因はREADMEではない」
その場合はほぼ確実に：

- READMEが `README.md` じゃない（例：`.txt`付き）
- GitHubが別ファイルをREADME扱いしている
- もしくは編集しているファイルが違う

なので、**次は確認だけ**します。

✅ GitHubのファイル一覧で、READMEはこう表示されていますか？

- `README.md`（これだけ）  
ではなく  
- `README.md.txt` や `README.txt` になっていませんか？

---

# 次の返事で教えて
1) いま貼った最小READMEで表示は直った？（はい/いいえ）  
2) GitHubの一覧でREADMEのファイル名は正確に何？（コピペでOK）

これで100%潰せます。

