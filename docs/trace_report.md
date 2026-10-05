# GoldEx 案：Picasso 的資金鏈上追蹤報告

查詢日期：2026-10-04（挪威時間）。時間都是**挪威時間**（夏季 CEST = UTC+2，冬季 CET = UTC+1）。

金額單位是 USDC 或 USDT，1 枚約等於 1 美元。地址和交易雜湊（tx）都可以在 etherscan.io（BTC 用 mempool.space）上直接查。每一跳的完整明細在 `hops.csv`（118 筆）。整體流向請看 `flow_diagram.png`。

---

## 一、先講結論

1. **全部在 Ethereum 主網。** Picasso 的 11 筆 USDC 入金都在 Ethereum 上，BTC 那筆在 Bitcoin 鏈上。BSC、Arbitrum、Polygon、Base 上都沒有找到相關交易。
2. **鏈上實際收到的金額：171,384.57 USDC，加上 0.0004273 BTC。** 跟 xlsx 有幾處小差異：
   - 8/18 鏈上是 1,509.3（xlsx 寫 1,519.3）
   - 9/12 鏈上是 25,867.0
   - 9/18 鏈上是 8,078.0
3. **詐騙方前後退給 Picasso 8 筆「提領」，共 26,598.79。** 這些錢主要是其他受害者的錢。其中 10/22 那筆 12,545.5 裡，有 10,000 是 Picasso 自己 10/20 存進去的錢，被原路退回。**鏈上淨損失約 144,785.78。**
4. **Picasso 的錢最後主要流到三個地方：**

| 最後去向 | 屬於 Picasso 的金額（約） | 這是什麼 | 信心 |
|---|---|---|---|
| **X1** `0xDA2142378e6dB3423965C14dE6F5D0876c69Af0a` | **≈ 50,782 USDT** | 大型洗錢樞紐。2025-08-29 到 09-30 經手約 5,700 萬 USDT。Etherscan 沒有標記；公開研究（tayvano / lazarus-bluenoroff-research）把它列為「被盜資金混合地址（Theft, Comingled）」。目前餘額 0。 | 中～高 |
| **X5** `0x11235534a66A33c366b84933D5202c841539D1C9` | **≈ 77,836 USDT**（另有約 7,700 可能也到這裡） | 高頻服務型地址：約 13 萬筆交易，2.7 天內經手約 1,900 萬 USDT，會呼叫「Bitget Wallet: Swap Bridge」合約。**沒有任何公開標記證明它是 Bitget 交易所帳戶**，Picasso 的 PDF 說是「BitGet」，**無法證實**。目前持有 **441,977 USDT，沒有被凍結**，到今天還在活動。 | 中 |
| **Y 系列 OTC 型錢包**（Y1/Y2/Y3/Y5） | **≈ 25,066 USDT/USDC** | 10–11 月 #5 地址的錢經出金錢包 C 和 R2 轉到這幾個未標記錢包，之後再分散出去。目前餘額都是 0。 | 中 |
| 退回 Picasso（假提領） | 10,000 | Picasso 自己的錢 | 高 |
| **Binance**（BTC） | 0.0004273 BTC | 跟另一位受害者的 0.1889 BTC 一起轉進 Binance 的 BTC 入金地址 | 高 |

5. **有沒有錢還「卡」在鏈上？**
   - Tether 在 **2025-10-16 15:41（CEST）凍結了 X2 和 X4**，目前凍結 **745,433.55 USDT**（X2 502,803.63，X4 242,629.92）。
   - 但用「最低中間餘額法」（LIBR，說明見第八節）計算，**Picasso 有明細的錢幾乎都在凍結之前就已經離開 X2/X4**。
   - 只有兩小筆**有可能**在凍結餘額裡：9/18 入金裡的 **6,000**（低信心），和 #5 地址 10/07 收到的 3,000（不在 xlsx 裡，可能不是 Picasso 的）。
   - 其他所有詐騙地址和中轉地址的 USDC/USDT 餘額都是 0 或幾十元。
   - 還持有大額 USDT 的未凍結地址只有 X5（441,977 USDT），但它是混合了大量資金的服務型地址，裡面不是「Picasso 的錢」。

---

## 二、地址對照表

標記來源：「ES」= Etherscan 公開名稱標籤（public name tag）；「推斷」= 由交易行為判斷。

| 代號 | 地址 | 角色 | 標記來源 |
|---|---|---|---|
| 詐騙入金 #1 | `0x9e4a53D4eBf53594Ac004Bcd3B443db17cB74B81` | GoldEx 給 Picasso 的入金地址（8/11） | 截圖 |
| 詐騙入金 #2 | `0xEF0776617364dd4Df0C1A12642D1a211E45C18bf` | 入金地址（8/18） | 截圖 |
| 詐騙入金 #3 | `0xc5D40064Bb1683A91ebE6117ACF4880a6a2D17A3` | 入金地址（8/22、8/25） | 截圖 |
| 詐騙入金 #4 | `0xdb685588535daba6c971450128f86d72c94f4002` | 入金地址（9/04、9/12、9/18） | 截圖 |
| 詐騙入金 #5 | `0xdca1bed54a13b4eaab1d8568935745becbfeca60` | 入金地址（10/20、10/30） | 截圖 |
| 詐騙 BTC | `bc1ptd59…`（見 xlsx） | BTC 入金地址，累計收過 2.27 BTC，現在餘額 0 | 截圖 |
| H1 | `0x0bFCe0574ee5ef4dAb2d6e7Bf0F1EB359DEF4AD1` | 歸集錢包，2025 年 2 月就開始活動 | 推斷 |
| H2 | `0xc5D0af894EE89E6304cD84048678556cE99Cb14C` | 歸集錢包 | 推斷 |
| R1–R8 | `0x9FC2813f…22D9`、`0xdb037e85…CCB0`、`0x505526C0…1134`、`0x0132683b…231a`、`0x0438DB3A…8E02`、`0x35F7db19…2627`、`0x7cBf20c3…c928`、`0xD33706b3…56E8` | 一次性或短期的中轉錢包 | 推斷 |
| X1 | `0xDA2142378e6dB3423965C14dE6F5D0876c69Af0a` | 大型洗錢樞紐 | ES 無標記；tayvano 研究列為 Theft (Comingled) |
| X2 | `0xfEF2a9E08D92Fb348485219DDb5322fE24960477` | 大型歸集樞紐，收很多受害者入金地址的錢；**USDT 已被 Tether 凍結** | Tether 合約事件 |
| X3 | `0xDe8d7BdD9C0e9182dc0bfD4Ab16A280871eb79A5` | X2 的下游 | 推斷 |
| X4 | `0x97915f7decbec83814afe9d6bfc773431942acc4` | X2/X3 的下游；**USDT 已被 Tether 凍結** | Tether 合約事件 |
| X5 | `0x11235534a66A33c366b84933D5202c841539D1C9` | 高頻服務型終點，未標記 | 推斷 |
| Y1/Y2/Y3/Y5 | `0xAddC0a707984978617d790D5B7CBdb3Abe834B53`、`0x53fF606a6D7116e18ee9Dca80824Fa0d70bCF1EB`、`0x132ED574f32B739feBF95d9D6Bd2f24001aEafDc`、`0xD4D63125735Eb997FAf89aDd73C48764134C39fE` | OTC 型中轉。Y5 在 X2 被凍結後接手 X2 的角色 | 推斷 |
| 出金錢包 A/B/C | `0xf68540248F124D871FE34941ba8936C2655EA5A6`、`0xd199416AF0882d9eFf042502adCF38F2d676eE46`、`0x0457DbCc707CAc75F9849153233F5b16B5aD67b1` | 付「提領」給 Picasso 的錢包 | 推斷 |
| Tokenlon | `0x4a14347083B80E5216cA31350a2D21702aC3650d` | Tokenlon AMM Wrapper（去中心化兌換）。詐騙方用它在同一錢包內把 USDC 換成 USDT | ES |
| Picasso 的 MEXC 入金地址 | `0xd6e7F03EbD4AAd7A0210fe08fe7ED1cbacc6cC18` | | 推斷（收 Picasso 的提領） |
| Picasso 的 Binance 入金地址 | `0xC803bbD1…AF2d` | | ES「Binance Deposit」 |
| Picasso 的 Crypto.com 入金地址 | `0xb15Fb9Fb…31dF` | 會歸集到 Crypto.com 16 | ES |

**這 5 個入金地址是同一夥人控制的（證據）：**

2026-04-18/19，#4、#3、#5、#2 把剩下的 ETH 掃到出金錢包 C：
- `0x1d1e231fc30cf895bbcdbed729f38f03fdb65dc91f842eb00f39d7e0262d29cc`
- `0xbb320d11906c3a434e4c0081d40586a95c4fa56e02ef17467410470d39656efc`
- `0x3f696a12d658ccbab5384151fb902ec55fb1ccb0fe3f01077f50cb95290ed709`
- `0x21e848458228a25b3d4d22ca010a3940ca5f26888ebf225d0546a962b264f72f`

另外，#4 也把 ETH 轉給 H2：
- `0x104d7e8456fad40f3b1e5a72773db222271c7ba45871ee7f23e76808181b9d21`
- `0xaffe66b2249907b5a3c7b108f2bfb2a34bd05d1f382f8a74cbac4eac58e81d9d`
- `0x59c006fe834cfa09943d8c7adec19d8a288f9b843d51f7d53329e317043d6348`

**注意「地址投毒」雜訊：** 有不少長得很像的假地址（例如 `0x0451…67b1`、`0x0457f9…`、`0x04575E…`）會發 0 元轉帳或假的「USDC」代幣。本報告只計算真正的 USDC 合約（`0xA0b8…eB48`）和 USDT 合約（`0xdAC1…1ec7`），假代幣全部排除。

---

## 三、Picasso 的入金（鏈上核對）

| 日期（挪威時間） | 從 | 到 | 金額 | tx |
|---|---|---|---|---|
| 2025-08-11 21:57 | Crypto.com 12（ES） | #1 | 90 USDC | `0xdb3691613c9cee0188dc9f1a196cfa9d052bd7f8e367920916e4b35823f29fc6` |
| 2025-08-11 22:30 | Crypto.com 12 | #1 | 1,304 | `0x727eaf960840ff6ee34fd4bde5e0bbab0aa23bc00ee7f1766c38c5339e0517fc` |
| 2025-08-18 18:12 | Crypto.com 12 | #2 | 1,509.3 | `0xdb485bcf43b5d30013dcaa1e836daefd28ccd87e7e9d658e72858d66690e0e25` |
| 2025-08-18 18:17 | Binance Hot Wallet 34（ES） | #2 | 3,208.08 | `0xd6924cb29e1e28f61172e78ec43ed2df15a0c9fdbd76ae2667901de0c7233192` |
| 2025-08-22 11:28 | Crypto.com 12 | #3 | 19,594.65 | `0xed5f0c90bc8d301d63b7cf991681e36c90ff1af94369719b96f44a5f3c129940` |
| 2025-08-25 16:36 | Binance Hot Wallet 34 | #3 | 1,566.40 | `0x3553a9bf3f6369a0eedd46acf22308bb8eef3c5dc218e566bfb24f15b36399ac` |
| 2025-09-04 11:41 | Binance Hot Wallet 34 | #4 | 75,101.12 | `0x64c6f7e7c0a02d555bd22e8e8873faeb716685aad6ca8cace44ef27166c15e9e` |
| 2025-09-12 22:53 | MEXC 16（ES） | #4 | 25,867.0 | `0xb6b2d38783fcbe5486f65fe438da833d9a74ae4565c5847ee7b828086f81b785`（xlsx 原本寫的 `0x627c…` 在鏈上不存在，已更正） |
| 2025-09-18 13:00 | MEXC 16 | #4 | 8,078.0 | `0xd522c121dfc56735caec450ad904721b9df3f0a6b8038a17720bddbf90552927` |
| 2025-10-20 15:33 | MEXC 16 | #5 | 29,954.36 | `0x94a2ef7a13f57c963c5fb0a85a9e69f4a16253e1af5960a56b40eaa4ed512aee` |
| 2025-10-30 22:17 | MEXC 16 | #5 | 5,111.66 | `0x9e265d21650c245683112bb98903496e0e6f96fcae0e861d6e79b32216771ab7` |
| 2025-08-11 22:01 | （Crypto.com 提領，依 xlsx） | 詐騙 BTC | 0.0004273 BTC | `ef634137e480498d75785721b7de5914f9fa50ca5813ba28e179aa83b1be6c27` |

**xlsx 裡沒有、但值得 Picasso 自己核對的入金：** 同一個 Crypto.com 12 熱錢包還轉了幾筆錢進 Picasso 的這幾個入金地址，共約 **8,424.59 USDC**：

| 入金地址 | 日期 | 金額 |
|---|---|---|
| #1 | 8/01 | 325.73 |
| #1 | 8/12 | 104.48 |
| #3 | 8/20 | 2,164 |
| #3 | 8/22 | 103.79 |
| #4 | 9/09 | 2,303.32 |
| #5 | 10/01 | 1,144.51 |
| #5 | 10/07 | 2,278.76 |

這些可能是 Picasso 自己的提領，也可能是其他人的。請 Picasso 對照 Crypto.com 的提領紀錄。

另外，`0xD66C7A0bb3eE0b4Ab9d9c532BeBa0219b4e73E44`（未標記）轉了小額進 #1 和 #3（共 186.43）。它也曾收過出金錢包 A 的 149.7，應該是其他受害者或詐騙方自己的錢包，不是 Picasso 的。

---

## 四、每一筆錢的去向（逐跳）

說明：
- 「FIFO」= 先進先出，先存進來的錢先被轉走。
- 「混合」= 這個錢包同時收了別人的錢，只能按比例或 FIFO 推算。
- 每一跳的完整 tx 都在 `hops.csv`，下面列出關鍵的幾筆。

### A 塊：#1、#2 和 #3 的一部分 → H1 → 大部分到 X1（Picasso 的份額 9,436.43；信心：低～中）

- 2025-09-01 21:49–21:53，#1、#2、#3 把餘額掃到 H1：
  - `0xc628f0b42325da4838347757ed4a76543eb3756e197b672fc2942c8a34cf1140`（1,964.21，其中 Picasso 的 1,394）
  - `0xa66eb6cc4846c3c5517716baed10cce718e19e89d951b809f51321fa9457815f`（4,717.38，全部是 Picasso 的）
  - `0x9a6d30bb19fd27dedf92fda34877193c6eea1cfc4499293319cae3eec518b909`（14,825.67，按 FIFO 其中 Picasso 的約 3,325.05）
- H1 在 Tokenlon 把 30,729 USDC 換成 USDT：`0x016d698c6bf4e42ce6b1000e7339fa863dd81a1a30ae144a84df3b226db3e535`
- 09-05 到 09-09，H1 一共轉出約 55,500：
  - 約 82% 經 R1/R2/R3/R4 進 X1，例如 `0x784dab26f2be98831ec4ae58e37833be51c6097995df7cdd06733361b88bc388`（20,000）
  - 10,000 經 R6 進 X2：`0x44a5a1be4768bd63e335e66a568a9ccfaa845b702caae69049ea55a0341e6693`
- **推估：** Picasso 的錢約 7,736 到了 X1，約 1,700 到了 X2（之後走 X3/X4 → X5）。

### B 塊：#3 → H2 → X2 → X3 → X4 → X5（17,836；信心：中～高）

| 時間 | 這一跳 | tx |
|---|---|---|
| 08-30 21:01 | #3 → H2，20,000 | `0xf143e33272b53db3691eefe36574b5cd87cc9b768aa9f7a9dfffdbfb4507b7a9` |
| 09-03 10:56 | H2 → X2，40,000 | `0x7eca0e916d05d02aa8084ce9373c3e8f754158e920d0c12c988e12bda09cdf73` |
| 09-03 10:57 | X2 換成 USDT | `0xb8d44217deb9f421474da23623411c181a80e2c8068fbca1bdf87afae061e1e9` |
| 09-03 11:00 | X2 → X3，192,986.91 USDT | `0xffc43c2d9b61284e5725fc946c7b518d1561d7f05392fd9e866be3681a6047a6` |
| 09-03 21:19 | X3 → X4，同額 | `0x756c8e334c6c9f1d5ecf79f7bd83dc483ee657db3e5d526549f73ed41f872f7b` |
| 09-03 21:20 – 09-04 10:32 | X4 → X5，50k + 50k + 50k + 42,986.91 | `0xc41768262de00d709328e1a25f18a72b468d08deaee67b84b9bb39160e5780ab`、`0xda563a066731278649098c44285f4faa59a985002fef6e36c293ff5115d60011`、`0xf616e1e18337e706db830c8a2675971f48f313ddf5d3020ea53d60748d1904a0`、`0x99af47b6a00179a1b500f66a1b140d2c0b062621da0a454547718e710e9b3b98` |

這條路線和 Picasso 的 PDF 裡列的 tx 一致。X4 在 09-04 餘額歸零，所以這塊錢不在 X4 被凍結的餘額裡。

### C 塊：#4 的 60,000 → H2 → X2 → X3 → X5（60,000；信心：中）

| 時間 | 這一跳 | tx |
|---|---|---|
| 09-04 18:27 | #4 → H2，60,000（Picasso 入金 6 小時後） | `0x0898e8948399df294ee8af09aef4d569f70a0cb283179b5f48f8e4a1bd4dd1fd` |
| 09-17 06:24 | H2 → X2，85,000（混了別人 25,000） | `0xf6d9e02e2808facad9d9950d0500582da29b8ad16802d1af67e6b78df339e5f4` |
| 09-17 15:58 | X2 換成 USDT | `0xd9b9978c51a5838c6fdbda3ba7687ca1baebd829ce438b62840fb471ae1d5988` |
| 09-22 05:34 | X2 → X3，578,645 USDT | `0xc25802aec834956e201f5856f8b0a834eb5acc51de5a64bf0eb4070f1b364d87` |
| 09-22 – 09-26 | X3 → X5，11 × 50,000 + 28,445 | 見 CSV |

### D 塊：#4 → R1 → X1（10,000；信心：高）

- 09-09 22:21，#4 → R1：`0x4fa425d35218d58e9b762035724defa154c43425647987b9f628f774967e9e38`
- R1 換成 USDT：`0x3cb62d0ee8956f0ce8db109ef26b4355ed4f52d35781f5da95b5a7abe2f5866a`
- 5,100 → R4 → X1：`0xe0abc28e8f9bcc497a42431b124994e5cc496f0e4a4d09c0d9e7593190beaee4`
- 4,000 → R2 → X1：`0x8140047766d19b517b6cc4ea527ebcd12f23aa7673ffcf526cf3f9025c87f9fc`
- 剩下約 900，之後也經 R2 進了 X1。

### E 塊：#4 → H1 → R3 → X1（23,007.24；信心：高）

- 09-15 22:35，#4 → H1，60,000：`0x501bafa59725ad6f56219c34c5ebdea14197834a3ab4fe1f50fd336936417f0a`
- H1 換成 90,000 USDT：`0x8338dfa2e54fad2e6d4506adb7d3463392d260313e04077ef3a5c60a5c4619d6`
- 整筆轉給 R3：`0xdc2670db98fe441f6e9903cc107db7f769b60af209ba941ecb806bb41e539734`
- 1 分鐘後進 X1：`0x4a4419eb554074c41f8e6bf03d0089fa6b8817ad53ab0a18989f342e6843a31e`

如果那筆 2,303.32 的 Crypto.com 入金也是 Picasso 的，這塊要再多 2,303。

### F 塊：#4 → H1 → X1（7,960.88；信心：中～高）

- 09-17 22:39，#4 → H1：`0x99455d27758e73747fa0e07f567a6be38a8c1a3556053494ef21bab693d9f2a1`
- 換成 USDT：`0x1b33d78d3373c1d27575f688f9c326f11b922c2d8168fe48295340a84ce63263`
- 再經 R4、R5、R2 進 X1：
  - `0x3dd6a83e6e3cf1881fe92aa52ed400ef1cec00574f4125cf5e97b0e7cfee13ad`
  - `0x93ea9b01f76d9b867e43a9fbfebe89df5cd7fecbde5c6174e264c656617b01c7`
  - `0x710d7970a36ee90255e5c64d6f7835888be5ddd132ee91bc63655ebc63ed548e`

### G 塊：9/18 的 8,078

**6,000 這部分（信心：低～中）：**
- #4 → 出金錢包 A：`0x545872545cb87caa5262e07bc1303c2c9fc1a3c357001643d9d8efbe6a711ae0`
- → `0x5A5c…`（未標記，有可能是第三方）：`0xc4f120bada7971e11e5b979020c927517f03bd607fb3e2b01e7d1f4ebdd72de7`
- → X2：`0x183b53ce7774bebeb3637ceaabb6c658a4a281335a63b37a030a275506c63fe7`
- 09-25，X2 → X4，671,236.59 USDT：`0x2dc599c0520a00a929eec7e28bfca6e56b9b6048d041f026d2b1f279d5d5b2da`
- 之後有兩種算法：
  - 按 FIFO：大部分隨後以每筆 5 萬分批到了 X5。
  - 按 LIBR：X4 從 09-25 到被凍結之前，最低餘額是 31,163（10/02），沒有低於 6,000。**所以這 6,000 理論上可能仍在 X4 被凍結的 242,629.92 USDT 裡。**這是本案唯一一筆有可能在凍結餘額裡的 Picasso 明細資金，但中間經過出金錢包 A 和 `0x5A5c…`，信心偏低。

**2,078.01 這部分（信心：中～高）：**
- #4 → R1：`0x009c0a56a35502751dea2032773497117c43972a441e864c54046ef9a10a9b9f`
- 換成 USDT → R2：`0xafc2f8cd77e0e8c67777228faff6e039bca493b0bc693fed8e3d27a9d79f212f`
- → X1：`0x14c41a859cb8dedce412b0a39ed28998f836e2ba259287b3e963ab2c5b23f5a5`

### H 塊：#5 的 35,066.02（10 月、11 月）

1. **10,000 退回 Picasso（信心：高）**
   - 10-21 21:27，#5 → 出金錢包 C：`0x674fd0d25cc1b8b7c9a4dc5680ab8811c7fb94c6b3aee55298707e2200215832`
   - 10-22 19:59，C 付 12,545.5 到 Picasso 的 MEXC：`0xe866041f40f998b40569ec8eaec0aaf06e950f5f7b5e8b8fb89e187673c1c083`
   - 也就是說，這次「提領」有 10,000 是 Picasso 自己的錢。另外 11,878.38 來自 `0xc847…`（未標記，它也替 #5 付 gas），tx `0xd068a8d54c765604a855c021c653ed9b861debcc05e242e40077da4d8a8178bf`。
2. **12,000 → Y1（信心：中～高）**
   - #5 → C：`0x04f3681b23363a813defe568c4b0b5d8de47163f9206b563f824d872506928f1`
   - C 換成 USDT → R2 → Y1：`0xdb1a90937138fae7cd870810a848da28adebeddd2891bff4cdc641593160dd8f`、`0xe9e5249daddc9959c555e7da86eb4e14de65f86856121413a011ea0496cea1f0`
3. **10,000 → Y2（Picasso 的份額約 9,815；信心：中）**
   - #5 → C：`0xd1b9dd82facf75c727154703f6eb2e2e1b397c44fb78538938835353aeef8721`
   - → R2 → Y2，12,069.20：`0x4d3f32f0e8a72aacd910ab3b372c2ed88ddb832f682202a7320323c435da2d0d`
4. **3,000 → R7 → Y5（信心：中）**
   - `0x5b524624ea2e967389aa4e95896692cc7370a5b87cda59d43bfc4c4218c00433`
   - `0x6e453e3104a7cc1574bfe05ff01965961b1398b81a997c7507022b47a2ef6e37`
5. **250.79 → C → R2 → Y3（信心：中）**
   - `0x7070cc02f1c2d7e6d4eff735b91920f8c74c1a9adbaf5249b176368fface56b2`

Y 系列錢包之後都把錢分散轉出，而且下游都沒有交易所標記，所以追到這裡為止。

### BTC：0.0004273 BTC → Binance（信心：高）

- 2025-09-01 03:17，詐騙 BTC 地址把 Picasso 的 0.0004273 BTC 和另一位受害者的 0.18888713 BTC 一起轉到 `13ZncoU2nomZStLChHJvefEjWm1kp14V3z`。tx：`9ea48a04bfa8007c599b29763245880f8c3b1c825ffbb008667c62b867a689a6`
- 這個地址隨後被歸集進 `bc1qm34lsc65zpw79lxes69zkqmk6ee3ewf0j77s3h`（chainquery 標為 Binance 儲備地址）。tx：`db8aef3eb7f2592e69c1325cf24ab990aec92fa0445ff45988618d1d70c424dd`
- 所以 `13ZncoU2…` 是某個 **Binance 用戶的 BTC 入金地址**。

---

## 五、凍結情況（Tether / Circle）

- **X2** 在 2025-10-16 15:41（CEST）被 Tether 加入黑名單。tx：`0x847fa8f460949cc930f34001e5dd10a4ebf9a7f75bd5cf3af9341e0d6f8ff863`。目前凍結 **502,803.63 USDT**。
- **X4** 同一時間被凍結。tx：`0x85dcc2a94d4b58598c72e0335de90da95c33fc24dc46b6e42cba1ee1a78f25de`。目前凍結 **242,629.92 USDT**。
- **USDC 的部分在凍結後逃走了：** 凍結 8 分鐘後，X2 把當時持有的 **543,892.26 USDC**（Circle 沒有凍結）轉給 Y5（`0xc6eebeacd535636159b11d9ea18e37059dbe5aee0ab5350765587f29402a3e54`）。Y5 換成 USDT 後，把 543,391.62 USDT 轉到 X3（`0x213cffc380d5409b5681f4895f87de385170d2670d4d5d9283ed90bf74aabe26`）。
- **凍結餘額裡有多少是 Picasso 的？** 用 LIBR 計算：
  - X2 的餘額在 9/10 和 9/25 都曾掉到 0 附近，這兩天都在 Picasso 的錢進入 X2 之後。
  - X4 在 9/04 歸零。
  - 所以 A、B、C 三塊都**不在**凍結餘額裡。
  - 只有 G 塊的 6,000 可能在 X4 裡（見上）。#5 在 10/07 收到的 3,000（屬於未列入 xlsx 的 Crypto.com 入金）經 R1 → R8 → X2，10/10 進入 X2，可能在 X2 凍結的 USDT 裡，也可能已經隨那批 USDC 逃走。
- **其他地址：** 檢查過的其他地址都沒有被 Tether 或 Circle 列入黑名單。

---

## 六、目前餘額（2026-10-04 查詢）

| 地址 | USDC | USDT | 備註 |
|---|---|---|---|
| 詐騙入金 #1–#5 | 0 | 0 | 只剩極少量 ETH |
| 出金錢包 A、C、H1、H2、R1–R3、R5–R8、X1、X3、Y1–Y5 | ≈ 0 | ≈ 0 | |
| 出金錢包 B `0xd199…` | 227.34 | 300.48 | 未凍結 |
| R4 `0x0132…` | 50 | 0 | 未凍結 |
| **X2** `0xfEF2…` | 0 | **502,803.63** | **已凍結（Tether）** |
| **X4** `0x9791…` | 0 | **242,629.92** | **已凍結（Tether）** |
| **X5** `0x1123…` | 1,050 | **441,977.09** | 未凍結，仍在活動，另有 23.25 ETH |
| 假稅地址 `0x225a8d7b…0d06` | 0 | 0 | 在 ETH、BSC、Arbitrum、Base、Optimism、Polygon 上都**從來沒有交易**。Picasso 沒有付錢到這個地址；也可能是從截圖抄寫時抄錯了一個字元 |

---

## 七、Picasso 收到的「提領」從哪裡來

| 日期 | 金額 | 從 → 到 | 付款 tx | 這筆錢的來源 |
|---|---|---|---|---|
| 08-12 | 733.31 USDC | A → Picasso 的 Crypto.com | `0x67076931f92654649258dba37f9f1814ae5754cd9a92d86ac349fd72db70cc03` | H1 的 2,000（`0x3b5efc180a243fa8c7c0ed22cda43b48211a1bdac0419bcd8bec394bc36079d9`），是混合的受害者資金。xlsx 裡寫的 `0xd5a31c…` 其實是 Crypto.com 的內部歸集 |
| 08-27 | 3,148.2 USDT | A → Picasso 的 Binance | `0xb4bed157eef89ba4def3379a2cfb9fcb05a941f5de9e8719530042fe11406870` | H1 的 10,000（`0xf43698128bba142958c4da75b96536f044a2be37f9cad448a031d2c2f8559dfc`） |
| 09-20 | 843.6 USDC | A → Binance | `0x16e738855ff34759a997949124ef6c1ceada565e0ba71c8416eac143e5afb20c` | A 的混合資金 |
| 09-21 | 2,997.99 USDC | A → Binance | `0x1662213bd1f52f5e1567dbd9962a11334ed0d9d25b1105bf502b63c4ab1092ff` | A 的混合資金 |
| 09-30 | 1,337.3 USDC | A → MEXC | `0x0dcc0f6e626eedb6e4aa2b43ea4aa646c2c994c42c6a78ebbcdda361fabb3f6d` | `0x5311…` 一分鐘前轉入的 1,500（`0x70db74f8394a8dd6a56687e07dc0f7612ef326fba888132af407e3f5e9c91e08`） |
| 10-06 | 961.93 USDC | B → MEXC | `0x98cb6187f9f6a9f521bf3a5fca6833ccbbe24b8f4b57f8a2512802e632aad9da` | B |
| 10-22 | 12,545.5 USDC | C → MEXC | `0xe866041f40f998b40569ec8eaec0aaf06e950f5f7b5e8b8fb89e187673c1c083` | **10,000 是 Picasso 自己的錢**，11,878.38 來自 `0xc847…` |
| 10-27 | 4,030.96 USDC | A → MEXC | `0x346b80bf3da828227bbe67862eedae8c5b1ecb90acd5da4772e7f2dc80971d23` | `0xcf59…` 的 5,000（`0xa1ceb39f692ea3d25c183029fa3c355fe725121d7d7cbfcc22bc95d33bce7dbf`） |

**合計 26,598.79。** 典型的「拿後面受害者的錢付前面受害者的提領」模式。

---

## 八、核對 Picasso 追蹤 PDF 裡的說法

| PDF 說的 | 鏈上查到的 | 結論 |
|---|---|---|
| OKX `0xBf94F0AC752C739F623C463b5210a7fb2cbb420B` | Etherscan 標記為「OKX 24」 | **確認是 OKX 錢包。** 但沒找到它和 Picasso 的錢有 USDC/USDT 的直接連接 |
| OKX `0xEbf6C883A1D60AB38c8ed4780aadBFE4c805Ed4F` | 智能合約錢包，資金來自「OKX 225」，很可能是 OKX 的提領錢包。09-08 它轉了 399.44 USDC **進** #4（`0xa007c0adbaeb21f53fd03437d83cda2315ef86c904b0ccabb204c6d823dd5223`）。PDF 寫成 339.44 | **是 OKX，但方向相反**：這是**別人從 OKX 存進**詐騙地址的錢，不是贓款流到 OKX |
| OKX `0x7a7ACda068BCDDA2B85f6a037B0285b5cfc8e3CA`、`0x2efa41F1A4E8234296509d24dB8d1802D347bd4f` | 兩者都會把錢歸集到「OKX: Hot Wallet 5」`0x5594…ed53`（`0x2efa` 也會歸集到 OKX 182/183），所以**確認是 OKX 的用戶入金地址**。它們的錢來自 `0x4AA7003c…ACa`，而這個地址是在 2025 年 3–7 月收到出金錢包 A 的款項 | **確認是 OKX 入金地址，但進去的不是 Picasso 的錢**：時間在 Picasso 第一次入金之前，應該是其他受害者或人頭帳戶在 OKX 出金 |
| Bitget `0x11235534…`（X5） | 未標記的高頻服務地址，會呼叫 Bitget Wallet 的兌換合約 | **無法證實是 Bitget 交易所帳戶** |
| Bitget `0x22cE84A7…b70A` | Etherscan 標記為「Bitget Wallet: Swap Bridge」，是去中心化的兌換/跨鏈路由合約 | **不是 Bitget 交易所帳戶**，錢不會停在這裡 |
| Bitget `0xb141f554188Cf306fDe443f6e991949636f80E49` | 未標記合約，有 11.6 萬筆交易，X5 會付錢給它 | **無法證實** |
| （PDF 圖裡出現的）`0x56Eddb…8b17F` | Etherscan 標記為「Binance 17」 | 是 Binance，但它在 PDF 那條流程中扮演什麼角色不明確 |
| Arkham 圖：「詐騙歸集錢包」 | 其中一個其實是 Binance 熱錢包 | 是誤判 |

---

## 九、方法與限制

- **資料來源：**
  - Ethereum：Blockscout（eth.blockscout.com）API 和 Etherscan 網頁上的公開名稱標籤
  - BTC：mempool.space、walletexplorer、chainquery
  - 公開研究：tayvano / lazarus-bluenoroff-research
  - Arkham 頁面被 Cloudflare 擋住，無法讀取，所以沒有用 Arkham 的標記。
- **追蹤規則：**
  - 優先追「金額相同、時間緊接」的轉帳（信心高）。
  - 碰到混合資金錢包時，用 FIFO 或按比例分配（信心中或低）。
  - 判斷「錢是否還留在某地址」時，用最低中間餘額法 LIBR：一個錢包的餘額一旦降到某個數字，裡面屬於某位受害者的錢就不可能超過這個數字。
- **為什麼停在 X1、X5、Y：**
  - X1 和 X5 每天經手數百萬美元，下游有成千上萬個地址，而且都沒有交易所標記。在這種地址之後再按比例分，結果已經沒有意義。
  - X5 很可能是某個 OTC 或兌換服務商的地址，但目前沒有公開證據指出是哪一家。
- **金額都是近似值。** 「Picasso 的份額」在混合錢包之後是推算的。直接一對一對上的部分（D、E、H1、BTC）信心最高。
