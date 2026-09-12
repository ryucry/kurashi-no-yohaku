import streamlit as st


# ページ設定
st.set_page_config(
    page_title="暮らしの余白",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# CSS設定
st.markdown(
    """
    <style>
    /* ページ全体 */
    .stApp {
        background-color: #f7f5f0;
    }

    /* Streamlit標準の余白を調整 */
    .block-container {
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* ヘッダー */
    .custom-header {
        width: 100%;
        max-width: 800px;
        margin: 0 auto 2rem auto;
        padding: 2rem 1.5rem;
        box-sizing: border-box;
        text-align: center;
        background-color: #ffffff;
        border-radius: 18px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
    }

    .custom-header h1 {
        margin: 0;
        color: #5f6658;
        font-size: 2rem;
        font-weight: 700;
        letter-spacing: 0.08em;
    }

    .custom-header p {
        margin: 0.8rem 0 0 0;
        color: #888f80;
        font-size: 0.95rem;
    }

    /* 見出し */
    h1, h2, h3 {
        color: #5f6658;
    }

    /* ボタン */
    .stButton > button {
        width: 100%;
        border: none;
        border-radius: 12px;
        padding: 0.7rem 1rem;
        color: white;
        background-color: #8b967f;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: #707d66;
        color: white;
    }

    /* 入力欄 */
    .stTextInput input,
    .stTextArea textarea,
    .stSelectbox div {
        border-radius: 10px;
    }

    /* フッター */
    .custom-footer {
        margin-top: 3rem;
        padding: 1rem;
        text-align: center;
        color: #999f94;
        font-size: 0.8rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ヘッダー
st.markdown(
    """
    <div class="custom-header">
        <h1>暮らしの余白</h1>
        <p>毎日の暮らしに、少しのゆとりを。</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ここからアプリの内容
st.subheader("今日の暮らし")

st.write("ここにアプリの内容を追加してください。")

# 例：入力欄
user_input = st.text_input("メッセージを入力してください")

if st.button("送信"):
    if user_input:
        st.success(f"「{user_input}」を受け付けました。")
    else:
        st.warning("メッセージを入力してください。")

# フッター
st.markdown(
    """
    <div class="custom-footer">
        暮らしの余白
    </div>
    """,
    unsafe_allow_html=True,
)

# 選択メニューを上部に配置
menu = st.selectbox(
    "カテゴリーを選択",
    [
        "一人暮らし必需品",
        "Wi-Fiとsim",
        "食",
        "生活必需品",
        "ふるさと納税"
    ],
    label_visibility="collapsed"
)
#各カテゴリーに移動先URLを設定
category_urls = {
    "一人暮らし必需品": "https://ryucry-kurashi-no-yohaku-app-jbr9xr.streamlit.app/",
    "Wi-Fiとsim": "https://example.com/wifi",
    "食": "https://example.com/food",
    "生活必需品": "https://example.com/daily",
    "ふるさと納税": "https://example.com/furusato",
}

#選択されたカテゴリーのURLを取得
selected_url = category_urls.get(menu)

#一人暮らし必需品を選択した場合
if menu == "一人暮らし必需品":
    st.markdown(
        f"""
        <a href="{selected_url}" target="_blank">
            <button style="
                padding: 10px 20px;
                font-size: 16px;
                cursor: pointer;
                border-radius: 8px;
                border: none;
                background-color: #4CAF50;
                color: white;
            ">
                一人暮らし必需品サイトを見る
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

import streamlit as st

#デザイン設定
st.markdown("""
<style>
.stApp {
    background-color: #171b1d;
    color: #f5f5f5;
    background-image:
        linear-gradient(rgba(100, 120, 125, 0.12) 1px, transparent 1px),
        linear-gradient(90deg, rgba(100, 120, 125, 0.12) 1px, transparent 1px);
    background-size: 52px 52px;
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="一人暮らし必需品",
    page_icon="🌿",
    layout="centered",
)

st.title("一人暮らし必需品")
st.write("新しい暮らしに揃えたいものを、選んでまとめよう。")
st.caption("すでに持っているものは選ばなくてOK。必要なものだけチェックしてください。")

categories = {
    "🛏️ 寝具": {
        "最優先": [
            "ベッドフレーム", "マットレス", "掛け布団",
            "枕", "シーツ", "枕カバー",
        ],
    },
    "🔌 家電": {
        "候補": [
            "冷蔵庫", "洗濯機", "電子レンジ",
            "炊飯器", "掃除機",
        ],
    },
    "🍳 キッチン用品": {
        "候補": [
            "フライパン", "鍋", "包丁",
            "まな板", "食器", "箸・スプーン・フォーク",
        ],
    },
    "🛁 バス・トイレ": {
        "最優先": [
            "バスタオル", "タオル", "バスマット",
            "お風呂ブラシ", "スポンジ", "トイレブラシ",
            "歯ブラシ", "トイレットペーパー",
        ],
        "ゆっくり": [
            "風呂いす", "湯おけ", "バスラック",
            "歯磨きコップ", "トイレマット",
        ],
    },
    "🧺 掃除・洗濯": {
        "最優先": [
            "物干し竿", "室内物干し", "ハンガー",
            "クイックルワイパー", "ランドリーバスケット",
        ],
        "ゆっくり": [
            "カーペットクリーナー", "洗濯機ラック",
            "洗濯ばさみ",
        ],
    },
    "📦 収納": {
        "最優先": [
            "収納棚", "テレビ台", "収納ボックス",
        ],
        "ゆっくり": [
            "傘立て", "突っ張り棚", "洗い物入れ",
            "ハンガーラック",
        ],
    },
    "🛋️ リビング": {
        "最優先": [
            "カーテン", "ゴミ箱", "ソファ", "椅子",
            "机", "ローテーブル", "ライト",
        ],
        "ゆっくり": [
            "クッション", "スリッパ", "ミラー",
            "時計", "観葉植物",
        ],
    },
}

st.info(
    "「最優先」「ゆっくり」は参考画像の目安です。"
    "すべて揃える必要はありません。"
    "ソファと椅子、机とローテーブルなどは、暮らしに合うものを選んでね。"
)
st.caption("ハンガーは「掃除・洗濯」にまとめています。")

selected = []

with st.form("shopping_form"):
    for category, groups in categories.items():
        st.subheader(category)

        for priority, items in groups.items():
            st.caption(priority)
            columns = st.columns(2)

            for index, item in enumerate(items):
                with columns[index % 2]:
                    checked = st.checkbox(
                        item,
                        key=category + "_" + item,
                    )

                if checked:
                    selected.append({
                        "category": category,
                        "priority": priority,
                        "item": item,
                    })

    st.subheader("✏️ ほかに揃えたいもの")
    extra_items = st.text_area(
        "一覧にないものは、1行に1つずつ入力してね。",
        placeholder="例：電気ケトル\n延長コード",
    )

    submitted = st.form_submit_button(
        "選んだものをまとめる",
        type="primary",
    )

if submitted:
    result = []
    seen = set()

    for entry in selected:
        if entry["item"] not in seen:
            result.append(entry)
            seen.add(entry["item"])

    for line in extra_items.splitlines():
        item = line.strip()

        if item and item not in seen:
            result.append({
                "category": "✏️ 追加したもの",
                "priority": "追加",
                "item": item,
            })
            seen.add(item)

    st.session_state["shopping_result"] = result

if "shopping_result" in st.session_state:
    result = st.session_state["shopping_result"]

    st.divider()
    st.header("📝 あなたの揃えるものリスト")

    if not result:
        st.info("まだ選ばれていません。必要なものをチェックしてね。")
    else:
        st.success(f"揃えたいものは、全部で {len(result)} 点です。")
        st.caption(
            "選び直したら、もう一度「選んだものをまとめる」を押してね。"
        )

        download_lines = [
            "暮らしの余白｜揃えるものリスト",
            f"合計：{len(result)}点",
            "",
        ]

        result_categories = list(
            dict.fromkeys(entry["category"] for entry in result)
        )

        for category in result_categories:
            st.subheader(category)
            download_lines.append(category)

            for entry in result:
                if entry["category"] == category:
                    label = entry["item"]
                    priority = entry["priority"]

                    st.write(f"・{label}（{priority}）")
                    download_lines.append(
                        f"□ {label}（{priority}）"
                    )

            download_lines.append("")

        st.download_button(
            label="📥 リストをテキストで保存",
            data="\n".join(download_lines).encode("utf-8-sig"),
            file_name="kurashi-list.txt",
            mime="text/plain",
        )
# おすすめ商品の設定
# 商品名・説明・URLは、後からここで変更できます。
# URLが空欄の間は、購入リンクを表示しません。

product_catalog = {
    "枕": [
        {
            "name": "枕の候補A（商品未登録）",
            "reason": "高さを調整できる商品を登録する枠です。",
            "rakuten_url": "",
            "amazon_url": "",
        },
        {
            "name": "枕の候補B（商品未登録）",
            "reason": "洗いやすさを重視した商品を登録する枠です。",
            "rakuten_url": "",
            "amazon_url": "",
        },
        {
            "name": "枕の候補C（商品未登録）",
            "reason": "価格を重視した商品を登録する枠です。",
            "rakuten_url": "",
            "amazon_url": "",
        },
    ],
    "冷蔵庫": [
        {
            "name": "冷蔵庫の候補A（商品未登録）",
            "reason": "省スペースな商品を登録する枠です。",
            "rakuten_url": "",
            "amazon_url": "",
        },
        {
            "name": "冷蔵庫の候補B（商品未登録）",
            "reason": "冷凍室の広さを重視した商品を登録する枠です。",
            "rakuten_url": "",
            "amazon_url": "",
        },
        {
            "name": "冷蔵庫の候補C（商品未登録）",
            "reason": "自炊向けの容量がある商品を登録する枠です。",
            "rakuten_url": "",
            "amazon_url": "",
        },
    ],
}

# 個別の商品をまだ登録していないアイテムにも、
# 仮の候補を3つ表示します。
def get_product_candidates(item):
    if item in product_catalog:
        return product_catalog[item]

    return [
        {
            "name": f"{item}の候補A（商品未登録）",
            "reason": "価格を重視した商品を登録する枠です。",
            "rakuten_url": "",
            "amazon_url": "",
        },
        {
            "name": f"{item}の候補B（商品未登録）",
            "reason": "使いやすさを重視した商品を登録する枠です。",
            "rakuten_url": "",
            "amazon_url": "",
        },
        {
            "name": f"{item}の候補C（商品未登録）",
            "reason": "デザインを重視した商品を登録する枠です。",
            "rakuten_url": "",
            "amazon_url": "",
        },
    ]


def show_shop_links(product):
    links = [
        ("楽天市場で見る", product.get("rakuten_url", "")),
        ("Amazonで見る", product.get("amazon_url", "")),
    ]

    has_link = False

    for label, url in links:
        url = url.strip()

        if url.startswith("https://"):
            st.link_button(label, url)
            has_link = True
        elif url:
            st.caption(f"{label}：URLを確認してください。")

    if not has_link:
        st.caption("購入リンクは準備中です。")


shopping_result = st.session_state.get("shopping_result", [])

if shopping_result:
    st.divider()
    st.header("🛍️ 選んだものから商品を探す")
    st.write("候補を見比べて、気になる商品を1つずつ選んでね。")
    st.info(
        "現在は画面確認用の仮の商品です。"
        "実在する商品のおすすめや性能評価ではありません。"
    )
    st.caption(
        "広告について：購入リンクを掲載する際は、"
        "この欄でアフィリエイト広告を含むことを明示します。"
    )

    chosen_products = []

    for entry in shopping_result:
        item = entry["item"]
        candidates = get_product_candidates(item)

        with st.expander(f"🔎 {item}の商品候補", expanded=True):
            columns = st.columns(3)

            for index, product in enumerate(candidates):
                with columns[index]:
                    st.markdown(f"**候補 {index + 1}**")
                    st.write(product["name"])
                    st.caption(product["reason"])
                    show_shop_links(product)

            options = ["まだ選ばない"] + [
                product["name"] for product in candidates
            ]

            choice_key = f"product_choice_{item}"

            if st.session_state.get(choice_key) not in options:
                st.session_state[choice_key] = "まだ選ばない"

            choice = st.radio(
                f"{item}はどれにする？",
                options,
                key=choice_key,
            )

            if choice != "まだ選ばない":
                selected_product = next(
                    product
                    for product in candidates
                    if product["name"] == choice
                )

                chosen_products.append({
                    "item": item,
                    "product": selected_product,
                })

    st.divider()
    st.subheader("🌿 あなたが選んだ商品")

    if not chosen_products:
        st.write("商品を選ぶと、ここにまとめて表示されます。")
    else:
        st.success(f"{len(chosen_products)}点の商品を選びました。")

        product_list_lines = [
            "暮らしの余白｜選んだ商品リスト",
            "",
        ]

        for chosen in chosen_products:
            item = chosen["item"]
            product = chosen["product"]

            st.markdown(f"**{item}：{product['name']}**")
            show_shop_links(product)

            product_list_lines.append(
                f"□ {item}：{product['name']}"
            )

        st.download_button(
            label="📥 選んだ商品名を保存する",
            data="\n".join(product_list_lines).encode("utf-8-sig"),
            file_name="kurashi-products.txt",
            mime="text/plain",
            key="download_chosen_products",
        )

    st.caption(
        "チェックリストを変更したら、上の"
        "「選んだものをまとめる」をもう一度押してください。"
    )
    st.caption(
        "選択内容は永続保存されません。"
        "残しておきたい場合はダウンロードしてください。"
    )

