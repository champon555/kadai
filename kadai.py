
# じゃんけんで石を溜めてガチャを引く。
import random
import tkinter as tk
from tkinter import messagebox

rank = ["S", "A", "B", "C"]
name = ["大当たり", "当たり", "普通", "残念"]
handlist = ["グー", "チョキ", "パー"]

class JankenGachaApp:
    def __init__(self, master):
        self.master = master
        master.title("じゃんけんガチャゲーム")
        self.stone = 0
        self.cl = 0
        self.win = 0
        self.get = []

        # 石の数表示
        self.stone_label = tk.Label(master, text=f"現在石の数は {self.stone} 個です。", font=("Arial", 14))
        self.stone_label.pack(pady=10)

        # メッセージ表示欄
        self.message_label = tk.Label(master, text="", font=("Arial", 12))
        self.message_label.pack(pady=10)

        # ボタンフレーム
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=10)

        # じゃんけんボタン
        self.janken_button = tk.Button(self.button_frame, text="じゃんけん", width=10, command=self.show_janken_options)
        self.janken_button.grid(row=0, column=0, padx=5)

        # ガチャボタン
        self.gacha_button = tk.Button(self.button_frame, text="ガチャ", width=10, command=self.show_gacha_options)
        self.gacha_button.grid(row=0, column=1, padx=5)

        # 終了ボタン
        self.quit_button = tk.Button(self.button_frame, text="終了", width=10, command=self.quit_game)
        self.quit_button.grid(row=0, column=2, padx=5)

        # じゃんけん手選択用フレーム（最初は非表示）
        self.janken_frame = tk.Frame(master)
        
        # ガチャ用フレーム（最初は非表示）
        self.gacha_frame = tk.Frame(master)

    def show_janken_options(self):
        # ガチャフレームを非表示
        self.gacha_frame.pack_forget()
        # 既存の手選択ボタンを消す
        for widget in self.janken_frame.winfo_children():
            widget.destroy()
        self.janken_frame.pack(pady=10)
        self.message_label.config(text="あなたの手を選んでください")
        for i, hand in enumerate(handlist):
            btn = tk.Button(self.janken_frame, text=hand, width=8, command=lambda h=hand: self.play_janken(h))
            btn.grid(row=0, column=i, padx=5)

    def show_gacha_options(self):
        # じゃんけんフレームを非表示
        self.janken_frame.pack_forget()
        # 既存のガチャ要素を消す
        for widget in self.gacha_frame.winfo_children():
            widget.destroy()
        self.gacha_frame.pack(pady=10)
        
        # 選択ラベル
        tk.Label(self.gacha_frame, text="ガチャを何回引きますか？", font=("Arial", 12)).grid(row=0, column=0, columnspan=2, pady=5)
        
        # 単発ボタン
        tk.Button(self.gacha_frame, text="単発（1回）", width=12, command=lambda: self.play_gacha(1)).grid(row=1, column=0, padx=5, pady=5)
        
        # 10連ボタン
        tk.Button(self.gacha_frame, text="10連", width=12, command=lambda: self.play_gacha(10)).grid(row=1, column=1, padx=5, pady=5)

    def play_janken(self, player_hand):
        cpu_hand = random.choice(handlist)
        result_msg = f"あなた：{player_hand}　相手：{cpu_hand}\n"
        if cpu_hand == player_hand:
            result_msg += "あいこです。石を入手できませんでした。"
        elif (player_hand == "グー" and cpu_hand == "チョキ") or \
             (player_hand == "チョキ" and cpu_hand == "パー") or \
             (player_hand == "パー" and cpu_hand == "グー"):
            result_msg += "あなたの勝ちです。石を10個入手しました。"
            self.stone += 10
            self.win += 1
        else:
            result_msg += "あなたの負けです。石を3個失いました。"
            self.stone -= 3
        self.update_stone_label()
        self.message_label.config(text=result_msg)
        self.janken_frame.pack_forget()  # 手選択ボタンを非表示

    def play_gacha(self, times):
        if self.stone >= 10 * times:
            self.stone -= 10 * times
            result_msg = f"石を{10 * times}個消費します。\n"
            
            for i in range(times):
                if self.cl >= 4:  # 5回に1回SランクかAランクが出るようにする
                    high = random.randint(1, 100)
                    if high > 50:
                        j = 0
                        self.cl = -1
                    else:
                        j = 1
                        self.cl = -1
                else:
                    num = random.randint(1, 100)
                    if num == 1:
                        j = 0
                        self.cl = -1
                    elif num < 12:
                        j = 1
                    elif num < 43:
                        j = 2
                    else:
                        j = 3
                result_msg += f"{rank[j]} {name[j]}\n"
                self.get.append(j)
                self.cl += 1
                
            self.update_stone_label()
            self.message_label.config(text=result_msg)
            self.gacha_frame.pack_forget()
        else:
            needed = (10 * times) - self.stone
            self.message_label.config(text=f"石が{needed}個足りません。じゃんけんで貯めてきて下さい！")

    def update_stone_label(self):
        if self.stone >= 10:
            self.stone_label.config(text=f"現在石の数は {self.stone} 個です。{self.stone//10}回ガチャを引けます。")
        else:
            self.stone_label.config(text=f"現在石の数は {self.stone} 個です。ガチャを引けません。")

    def quit_game(self):
        messagebox.showinfo("終了", f"今回あなたは{self.win}回じゃんけんに勝って、ガチャを{len(self.get)}回引きました。\n獲得した大当たりの数は{self.get.count(0)}個でした。")
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = JankenGachaApp(root)
    root.mainloop()

