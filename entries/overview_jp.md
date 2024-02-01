---
title: カレンダーのバージョン管理
entry_root: overview_jp
publish_date: July 1, 2019
orig_publish_date: March 25, 2016
---

*CalVerは、任意の数字ではなく、プロジェクトのリリースカレンダーに基づいたバージョン管理規約です。*

**バージョン管理は時間と共に改善されます。**

メンテナにとって、バージョン管理は、拡大し続けるエコシステムの中で正確な依存関係を特定することを可能にします。
販売者やプロモーターにとって、プロジェクトのバージョンはブランドの動的な一部です。
私たち全員にとって、バージョニングは過去を参照しながら未来へ向けてアップグレードすることを可能にします。

プロジェクトによってバージョニングのシステムは異なりますが、共通の慣行があります。
たとえば、ポイントで区切られた数字（たとえば、*3.1.4*）は、すべて決まっています。
もう1つの一般的なバージョニングパターンは、時間ベースの要素（通常はリリース日の一部）を組み込んだものです。

この日付ベースのアプローチは、Calendar Versioning、略して**CalVer**と呼ばれるようになりました。

[TOC]

# スキーマ

カレンダーのバージョン管理方式は複数あり、大小のプロジェクトで長く使われてきました。
一つの方式を CalVer と宣言するのではなく、それぞれの実用性を認識し、プロジェクトに合った[スキーマを設計][designing_a_version]することが重要です。まず、バージョンのパーツを示します。

* **Major** - バージョンの最初の数字。2と3はPythonの有名なメジャーバージョンです。メジャー区分は、最も一般的なカレンダーベースのコンポーネントです。
* **Minor** - バージョンの2番目の数字です。7は、Pythonの最も人気のあるマイナーバージョンです。
* **Micro** - バージョンの3つ目、通常は最後の数字です。パッチ "セグメントと呼ばれることもあります。
* **Modifier** - "dev", "alpha", "beta", "rc1 "などのオプションのテキストタグです。

最近のバージョン識別子の大半は、2つか3つの数字セグメントとオプションの修飾子で構成されています。
慣習的に、4つの数字からなるバージョンは推奨されません。

[designing_a_version]: http://sedimental.org/designing_a_version.html

以下の[ケーススタディ](#ケーススタディ)に見られるように、プロジェクトはバージョンで日付を活用する有用な方法を複数発見しています。
CalVerは、単一のスキームを選択するのではなく、「セマンティック」バージョンに加え、開発者のための標準的な用語を導入しています。

* **`YYYY`** - Full year - 2006, 2016, 2106
* **`YY`** - Short year - 6, 16, 106
* **`0Y`** - Zero-padded year - 06, 16, 106
* **`MM`** - Short month - 1, 2 ... 11, 12
* **`0M`** - Zero-padded month - 01, 02 ... 11, 12
* **`WW`** - Short week (since start of year) - 1, 2, 33, 52
* **`0W`** - Zero-padded week - 01, 02, 33, 52
* **`DD`** - Short day - 1, 2 ... 30, 31
* **`0D`** - Zero-padded day - 01, 02 ... 30, 31

従来のバージョン番号は0始まりであるのに対し、日付セグメントは1始まりであること、また、短い年号と0パッドは2000年を基準にしたものであることに注意してください。
また、週は通常月/日と排他的に使用されることに注意してください。

[グレゴリオ暦][gregorian] を想定しており、[UTC][utc]も同様である。
技術的には、プロジェクトでどの暦を使用するかを明記すれば、どのような暦でも使用することができます。

[gregorian]: https://en.wikipedia.org/wiki/Gregorian_calendar
[utc]: https://en.wikipedia.org/wiki/Coordinated_Universal_Time

# ケーススタディ

CalVerはかなりの数のユーザーを抱えています。
これらは、注目度や使用事例の多様性から選ばれたプロジェクトです。

## Ubuntu

<img src="https://img.shields.io/badge/calver-YY.0M.MICRO-22bfda.svg" />

**[Ubuntu][ubuntu]**は、最も著名なLinuxベースのオペレーティングシステムの1つで、短い年とゼロパディングされた月を持つ3セグメントで構成されたCalVerスキームを使用しています。
2004年10月、Ubuntuの[最初の一般リリース][ubuntu_releases]となる4.10では、当初からそうしていた。

単純なオペレーティングシステムでさえ、多くの部品があり、任意の数字で多くの意味を伝えることは困難です。
プロジェクトのリリースに日付を入れることで、カレンダーベースのバージョンは任意の数字以上の意味を持ち、単純な事実に根ざした有益な情報を伝えることができるのです。

Ubuntu は、その CalVer スキームをサポートスケジュールと統合することで、さらなる利益を得ています。
Ubuntuは現在、長期サポート（LTS）リリースのサポート期間を5年とし、LTS以外のリリースは9ヶ月のみとしています。
CalVerと初歩的な算数のおかげで、どんなユーザーでも自分のバージョンがまだサポートされているかどうかを簡単に判断することができます。
本稿執筆時点の現在のLTSリリースである16.04は、2021年4月までサポートされる予定です。

[ubuntu]: http://www.ubuntu.com/
[ubuntu_releases]: https://en.wikipedia.org/wiki/List_of_Ubuntu_releases

## Twisted

<img src="https://img.shields.io/badge/calver-YY.MM.MICRO-22bfda.svg" />

Pythonのネットワークと非同期実行フレームワークとして有名な**[Twisted][twisted]**は、3セグメントのCalVerスキームを使用しており、メジャーバージョンのスロットには短い年、マイナーバージョンのスロットには短い月、3番目と最後のスロットにはマイクロ/パッチのバージョンがあります。

2002年に初めてリリースされ、現在も活発に開発されているTwistedは、その大きなスコープに見合った成長を遂げた[成熟][twisted_wp]したライブラリです。
IRC クライアントから HTTP サーバ、並列プログラミングのための多数のユーティリティに至るまで、あらゆるものを備えています。
オペレーティングシステムのように、Twistedには多くのパーツがあり、個々のパーツが非推奨で互換性を失うため、SemVerの適合性は低くなっています。

Twistedの非推奨のパーツは、連続する各バージョン間で後方互換性があり、破壊的な変更は時間単位で行われます。

このバージョン管理方式は、[Klein][klein]、[Treq][treq]、そしてTwistedの依存関係の1つである[PyOpenSSL][pyopenssl]などの関連プロジェクトにも広がっています。

[twisted]: https://twistedmatrix.com
[twisted_wp]: https://en.wikipedia.org/wiki/Twisted_%28software%29
[klein]: https://github.com/twisted/klein
[treq]: https://github.com/twisted/treq
[pyopenssl]: https://github.com/pyca/pyopenssl

## youtube-dl

<img src="https://img.shields.io/badge/calver-YYYY.0M.0D-22bfda.svg" />

**[youtube-dl][youtube-dl]**は、あらゆるインターネットメディアアーキビストの控えめな味方ですが、フルイヤー、ゼロパッドの月、ゼロパッドの日を含む3セグメントのCalVerスキームを使用しています。
このバージョンは、一部の技術的な文脈で追加されるマイクロセグメントを除き、ほぼ完全にカレンダー駆動です。

youtube_dl という名前にもかかわらず、その範囲は広大です。
長く、拡張し続けるサイトのリストから音声やビデオを抽出することをサポートしています。
対応するサービスのリリースサイクルが早いことを考えると、このプロジェクトがなぜこれほどまでにCalVerを採用しているのかがよくわかります。

[youtube-dl]: https://youtube-dl.org/

## pytz

<img src="https://img.shields.io/badge/calver-YYYY.MINOR-22bfda.svg" />

**[pytz][pytz]** は [IANA/Olson タイムゾーンデータベース][iana_tz]の Python 翻訳で、コンピュータ世界のすべての正確な時刻を支えるデータベースです。

Pythonは "battery-included "アーキテクチャの歴史があり、datetimeモジュールは頻繁にタイムゾーンに言及しますが、Pythonのコアランタイムはタイムゾーン情報を含んでいません。
これは、タイムゾーンの更新が決まったスケジュールに従わず、政治や立法の気まぐれに左右されるためです。
カレンダーのバージョニングは、そうでなければ無秩序なシステムの日付スタンプのスナップショットを提供します。

[pytz]: https://pypi.python.org/pypi/pytz
[iana_tz]: https://www.iana.org/time-zones

## Teradata

<img src="https://img.shields.io/badge/calver-YY.MM.MINOR.MICRO-22bfda.svg" />

**[Teradata UDA クライアント][teradata_uda]** は、[Teradata][teradata]のデータウェアハウス技術への[次世代アクセス][uda_blog]を提供します。

Teradataの使い方が注目されるのは、技術や企業の著名さではなく、2016年に15.10とバージョン表記されたリリースが複数回あったためです。これは、最初は破たんしているように見えるかもしれませんが、その意味と効用は明らかです。

ライブラリのメンテナは、[セマンティックバージョニング][semver]とカレンダーバージョニングの機知に富んだハイブリッドを作り上げました。
バージョンの**YY.MM**の部分は、SemVerのメジャーバージョンを組み合わせたものとして使用されます。
つまり、新しいリリースの場合、ライブラリのAPIは2015年10月と同じままである。
それ以降に書かれた依存関係のあるコードはバージョンアップしても問題ありません。
次回、APIのブレークイングの変更があったときに、年月のセグメントが更新されるのを確認する予定です。

[teradata]: http://www.teradata.com/
[teradata_uda]: https://pypi.python.org/pypi/teradata
[uda_blog]: https://developer.teradata.com/tools/reference/teradata-python-module
[semver]: http://semver.org/

## その他の代表的なプロジェクト

* [Unity][unity] - **`YYYY.MINOR.MICRO`** - クロスプラットフォームゲームエンジン.
* [pip][pip] - **`YY.MINOR.MICRO`** - Pythonオフィシャルパッケージマネージャ.
* [PyCharm][pycharm] - **`YYYY.MINOR.MICRO`** - 著名なPython IDE.
* [OpenSCAD][openscad] - **`YYYY.0M`** - 3D CAD モデリングのための最高のOSS.
* [fusefs-ntfs][fusefs-ntfs] - **`YYYY.MM.DD_MICRO`** - システム用の最も初期で最も相互互換性のあるNTFSアクセス層の1つ.
* [certifi][certifi] - **`YYYY.MM.DD`** - certifi は Mozilla の認証局バンドルのラッパーで、安全なインターネット通信に使用されます. [pytz](#pytz) と同様に、証明書の更新は固定されたスケジュールに従って行われませんが、タイムリーで日付指定可能な更新はセキュリティにとって重要です.
* [boltons][boltons] - **`YY.MINOR.MICRO`** - Python標準を補完する幅広いユーティリティライブラリ.

[unity]: https://unity3d.com/unity/whats-new/
[pycharm]: https://www.jetbrains.com/pycharm/download/
[fusefs-ntfs]: http://www.freshports.org/sysutils/fusefs-ntfs
[openscad]: http://www.openscad.org/
[certifi]: https://pypi.python.org/pypi/certifi
[boltons]: http://boltons.readthedocs.io/en/latest/
[pip]: https://pip.pypa.io/en/stable/news/

CalVerユーザのリストは成長しています。詳しくは [Usersページ][users] をご覧ください。

[users]: /users.html

# いつCalVerを使うべきか

もし、あなたとあなたの知らない人の両方があなたのプロジェクトを真剣に使うのであれば、真剣にバージョンを使ってください。
幸いなことに、そのバージョンに CalVer を使うかどうかの判断は、これまで以上に簡単にできるようになりました。

* あなたのプロジェクトの特徴は、スコープが大きいか、常に変化していますか？
    * [Ubuntu](#ubuntu) や [Twisted](#twisted) のような大規模なシステム、フレームワーク
    * [Boltons](#other_notable_projects)のような非定形のユーティリティ・セット
* あなたのプロジェクトは時間的制約がありますか？他の外部環境の変化により、新しいプロジェクトがリリースされることがありますか？
    * [Ubuntu](#ubuntu)がサポートスケジュールに重点を置いているような、ビジネス要件
    * セキュリティの更新、たとえば[certifi](#other_notable_projects)の証明書更新の必要性
    * 政治的な変化、たとえば[pytz](#pytz)のタイムゾーンの変更への対応など

もし、これらの質問のどれかにイエスと答えたのなら、 CalVer のセマンティクスはあなたのプロジェクトにとって強力な 選択肢となるでしょう。
