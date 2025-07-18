# -*- coding: utf-8 -*-

#じゃんけんで石を溜めてガチャを引く。
import random
rank=["S","A","B","C"]
name=["大当たり","当たり","普通","残念"]
handlist=["グー","チョキ","パー"]
stone=0#石の数
cl=0#天井値の設定
win=0#じゃんけんに勝った数
get=[]
while True:
  print("現在石の数は",stone,"個です。")
  check1=input("じゃんけんをするかガチャを引くか選んでください。やめる際は0を入力してください。")#ボタン押すだけにしたい
  if check1==("じゃんけん"):#じゃんけんに勝つと石を回収できる。負けると減る。
    cpu=random.choice(handlist)
    hand=input("あなたの手をグー、チョキ、パーの中から1つ入力してください。それ以外を入力すると負け扱いになります。")
    if cpu==hand:
      print("あなた：",hand,"相手：",cpu,)
      print("あいこです。石を入手できませんでした。")
    elif (hand=="グー" and cpu=="チョキ") or (hand=="チョキ" and cpu=="パー") or (hand=="パー" and cpu=="グー"):
      print("あなた：",hand,"相手：",cpu,)
      print("あなたの勝ちです。石を10個入手しました。")
      stone=stone+10
      win=win+1
    else:
      print("あなた：",hand,"相手：",cpu,)
      print("あなたの負けです。石を3個失いました。")
      stone=stone-3
    if stone>=10:
      print("現在の石の数は",stone,"個です。",stone//10,"回ガチャを引けます。")
    else:
      print("現在石の数は",stone,"個です。ガチャを引けません。")
  elif check1==("ガチャ"):
    times=int(input("ガチャを何回引きますか？"))
    if stone>=10*times:#天井が低めの設定なので10連でのAランク保証は無し。10連も貯まらない。
      print("石を",10*times,"個消費します。")
      stone=stone-(10*times)
      for i in range(times):
        if cl>=4:#5回に1回SランクかAランクが出るようにする。地味に貯まらない。
          high=random.randint(1,100)
          if high>50:
            j=0
            cl=-1
          else:
            j=1
            cl=-1
        else:
          num=random.randint(1,100)
          if num==1:
            j=0
            cl=-1
          elif num<12:
            j=1
          elif num<43:
            j=2
          else:
            j=3
        print(rank[j],name[j])
        get.append(j)#取得したランクをリストに入れて、終了時に結果発表
        cl=cl+1
    else:
      print("石が",(10*times)-stone,"個足りません。じゃんけんで貯めてきて下さい！")
  elif check1=="0":
    print("終了が選択されました。ゲームを終了します。")
    print("今回あなたは",win,"回じゃんけんに勝って、ガチャを",len(get),"回引きました。獲得した大当たりの数は",get.count(0),"個でした。")#終了までに獲得したSランクの数を表示
    break
  else:
    print("不正な入力が行われました。入力しなおしてください。")
