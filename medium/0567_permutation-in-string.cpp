// https://leetcode.com/problems/permutation-in-string

#include <test-registry.h>

#include <array>
#include <cassert>
#include <cstddef>
#include <functional>
#include <stdexcept>
#include <string>
#include <string_view>
#include <unordered_set>

namespace {

using InputT   = std::string_view;
using SymbolT  = InputT::value_type;
using CounterT = std::size_t;

using SymbolSetT = std::unordered_multiset<SymbolT>;
using SolutionFn = std::function<bool(const InputT&, const InputT&)>;

// T = O(N*K): N - permut.length(), K - text.length();
// S = O(N):   N - permut.length();
bool slow_IsContains(const InputT& text, const InputT& permut) {
  const auto permutSet  = SymbolSetT{permut.cbegin(), permut.cend()};
  const auto permutSize = permutSet.size();

  for (auto idx{0U}; (idx + permutSize) <= text.length(); ++idx) {
    const auto textSet = SymbolSetT{text.begin() + idx, text.begin() + (idx + permutSize)};

    if (textSet == permutSet) {
      return true;
    }
  }

  return false;
}

class SymbolCounter final {
public:

  // T = O(N): N - input.length();
  // S = O(1);
  explicit SymbolCounter(const InputT& input) : m_inputLength{input.length()} {
    for (const auto symbol : input) {
      m_inputCounters.at(toIndex(symbol)) += 1;
    }
  }

  // T = O(1);
  // S = O(1);
  auto inputLength() const noexcept {
    return m_inputLength;
  }

  // T = O(1);
  // S = O(1);
  void replaceSymbol(const SymbolT from, const SymbolT to) {
    if (from != to) {
      m_inputCounters.at(toIndex(from)) -= 1;
      m_inputCounters.at(toIndex(to)) += 1;
    }
  }

  // T = O(1);
  // S = O(1);
  bool operator==(const SymbolCounter& rhs) const noexcept {
    if (this == &rhs) {
      return true;
    }

    auto idx{0U};
    for (const auto thisValue : m_inputCounters) {
      const auto rhsValue = rhs.m_inputCounters.at(idx++);
      if (thisValue != rhsValue) {
        return false;
      }
    }

    return true;
  }

  // T = O(1);
  // S = O(1);
  bool operator!=(const SymbolCounter& rhs) const noexcept {
    return not(rhs == (*this));
  }

private:

  static constexpr auto ASCII_CODE_START = 'a';
  static constexpr auto ASCII_CODE_END   = 'z';
  static_assert(ASCII_CODE_END > ASCII_CODE_START);

  static constexpr auto ASCII_CODE_AMOUNT = (ASCII_CODE_END - ASCII_CODE_START) + 1;
  static_assert(ASCII_CODE_AMOUNT == 26);

  // T = O(1);
  // S = O(1);
  static SymbolT validate(const SymbolT symbol) {
    if ((symbol < ASCII_CODE_START) or (ASCII_CODE_END < symbol)) {
      throw std::out_of_range{std::string{}};
    }
    return symbol;
  }

  // T = O(1);
  // S = O(1);
  static std::size_t toIndex(const SymbolT symbol) {
    return (validate(symbol) - ASCII_CODE_START);
  }

  std::size_t m_inputLength;
  std::array<CounterT, ASCII_CODE_AMOUNT> m_inputCounters{};
};

const auto test_SymbolCounter = [] {
  {
    try {
      SymbolCounter{"aAa"};
      assert(false);
    } catch (const std::out_of_range&) {
      ;
    }
  }

  {
    assert(SymbolCounter{std::string_view{}}.inputLength() == 0);
    assert(SymbolCounter{"a"}.inputLength() == 1);
  }

  {
    auto a = SymbolCounter{"xxyyzz"};
    auto b = SymbolCounter{"zyyyyz"};

    a.replaceSymbol('x', 'y');
    assert(a != b);

    a.replaceSymbol('x', 'y');
    assert(a == b);
  }

  return true;
}();

// T = O(N + K): N - permut.length(), K - text.length();
// S = O(1);
bool fast_IsContains(const InputT& text, const InputT& permut) {
  if (text.length() < permut.length()) {
    return false;
  }

  const auto permutCounter = SymbolCounter{permut};

  const auto* textSliceBegin = text.cbegin();
  const auto* textSliceEnd   = textSliceBegin + permutCounter.inputLength();

  auto textCounter = SymbolCounter{{textSliceBegin, textSliceEnd}};

  while (textSliceEnd != text.cend()) {
    if (textCounter == permutCounter) {
      return true;
    }

    textCounter.replaceSymbol((*textSliceBegin), (*textSliceEnd));

    textSliceBegin = (textSliceBegin + 1);
    textSliceEnd   = (textSliceEnd + 1);
  }

  return (textCounter == permutCounter);
}

const std::string_view kLongText =
"lkrzcpwilhhuukffdtbajghpqrjsypwzkuviqhbxtnzlubuzyveujbnljkttzwmjdrukrzes"
"wttdzjfvqrlfzztguavagwcugmmhxjdqpoagxemkvhfnhgclsejzfsfttiwvjmfqufqoprdb"
"egoqoucaxyylxmwfbmkujckwnnskxvkedowmwvabmdkeeclvjubydnihymgrdzodajprsfao"
"dwqovmgmzrvtsshlbkbthbheumgsknwqbdqohxkkbxjsmicwlujfpilukllevoleztzxpplw"
"cwsngpbhugofynxnbhfkngxjfmovhzsxftjthzytgpnejbnfqbeowjanppgxkqnxxdkpakqv"
"pkbefthbiemgwwifskvysbmbhuoheqrgqpyaziuiwwhhduzorzqggiffxxhdihzxdncvrlvz"
"itiewgwlbgylufpianpekzhwlecdhyrubcttfruxmzfukiirciagaqchvluyjsmzvpahtrta"
"isuzrqagutlasdgbxvqyqhhxozzyxouxfrvikrfaawneoyyornaxbcizbrhtytwrljwazykl"
"ydnsviwfcfgrkawirkhoyhrbpppifbdnknkqdkzmbcfrmqkbsziarbwadssrliujdgwrxjod"
"uyancvsabuqrmgyppjnkxvuthzquaxsbxkdsavvrgyxsklfizfsycyrnhymmbjcxvhlcxqpe"
"atipzxdzfayuqhvudbpwoowcvbwpjgfiigrskssigdnuuhhfxrrcdvtmnsverwpnjefnzirg"
"hlxnizusztvjawchiecdgtsawogxdxjaewgiyabjywhhnkfbdrucihhxopxmxrxyslcumfsr"
"urnsybwcebxrcqlmthilndrfwzvvsqirsqmryluwavjjlvdstefpxylinmxgmvlzjoewwpra"
"cbkixoapezvdsjoamarnsgzufzdgxteypomrqqkazsxrbvkmviisvanumskxkpzrrvmletqa"
"nboionifpdszyleowjagagglnamwmopfindniokvkydsnayaezdmjfkbrfwuxbaoxicnoxfa"
"kwjmvfchqtnifuwtswwvvxircuzuhdobdqkzmczenfptpihpzhorjlqpqudijfqwzikwnhcz"
"kualaxiuebctizkqtcrxkpemzugpfpbaybsflzsvwnlnysnwsnlrdmtcrdgwurgioobcwjro"
"iqlbsdcvemzaqtffiliwerqdispranlcvdyemmyyogrwbxqqghxoqytjnrzrdioejilthxpz"
"kjbhjztasjvknjoklgwhtegujxvkcykabablssobxsyrkcjjobmkkfbyhwkztpnlgljqzydl"
"uiskkegngrzrkebbmufhglaqslieeosbywehrgtkfugaxzdsxnlcfudkdqqgjtvtxifbhjzn"
"jibqvvukkpsjttsexpqbpampciqoyxhiaciqdrwlliogcmfcbcxcqzhvvkmjbpmqgaxumaub"
"jebxoanitykumqugkflemefahqvppjirmehsiyzgeguwoycquwyyyilmwmazcrldnivlnrob"
"lupdljmeaqzkwyuiufcvlazrthrhzbuucpmsummwhdjeqlzmsderjdekpuxovgucwnnmxcrk"
"kaqnhlobdzdtpkpqtmhihrngnrygazklcpayqkfplqtcjfxejtpownqadaqwitghcykhxage"
"vcsehinojnyfzqgaxulavxrkxunynztsnrdeciqkyuthqgtytatpvagbqnvbknailnesqqmu"
"ghpeiqqkgfxuhxwqwgfrfgauiuqyyhupwccoosyvvvqbndxcptlncdpircgxyhxujqnaamxo"
"yggyszbtbidggomlxzfyqlwlzrtjheckedypwcmyugvexfpnvagoebfmfrjcxbzaopvwggxh"
"ozpljvzdfmdotvczdbzavacgalwgdbjcjtzdxkdgtxzojyeixgaxluddgpqzzmilruccxacq"
"qfgvlhdwmqwmmoacyamjlamcjkrfugbmzfdgdgmywyjexnnhuqixgyorzjzkyarvnkqcfnso"
"hfuhlqdzjmsmdzrgcjqdevltghvtjfkcckeiesbldwjjarkjaocpwubzwqnuqikydqatbvok"
"axtbxakmrobpnzavjzctgjogmnbnjpvlmwlzrxutszuvtkrbxejyklaeqprhhcixtmonmvvh"
"qhuqjffvmjjycgrgkdrlxkabymcuhesisrqmbumkjqxfeydpbbjflkteblsyscmibgiqovrx"
"mvbejmjaztimulmoclmjwbepasijdlwuvirzbxrucawcipmpxrekogcuctkjabzuhwiefver"
"eeyjbxproizfipckidjaybvymiwpeuiqcatokgdeedufezzbkwcqqocfqquecofkzjlshjhg"
"khavgltyuxdhkxddhyddgttzddofhbtmlsykfcoffxfhgfcuntegtwvxfkkitogwkpgidtmb"
"ckbddialbloyswuvtspzwqygllsnczknbtluooxquzbefgpbldjeowdxtvnyertifubiuyyu"
"oqkqcpvszrutjmuywyxabwzfdvodkyzrbthoemktxedeuevzgwstdvfsskqusecqgymzzboh"
"avgvtgrhxvvturrqxwtwgghbpnvftrqsnktgczshbdoabtptehehaoisrwzmbtvpzphzwhvx"
"auswemkkgqexnedlzwaxhuhbybnwldcpkbxalccoymlhqqjyzhwrkukgvyuefvjargjkxnue"
"rbywamzpbhottksicixcumvtypaogmtxjshajptmpicjmrpmytzqiihiecvufqoqthdmwfly"
"dwwcfqrnschgdrciweyfvxcpyebixanzixahhudrtrxtuhvfdyzwapcabpfunjmmvhufsdkn"
"cqensiibrfjijvsxjdqzclcaiyoebiatmnmiufbtjnhschoxboojjagijficguwpluyyqosp"
"rjahcqdibeckzbxoezbiglakdwrcnmjanilmudvqivxnifrrbgmpyjfwujupzalhrhptiplx"
"vsuoybzlyoyqdjcpgxmapxftbojsqwnaedfefufvvaipnsghylbqdnomkhbrraikxnmvancq"
"doihitpksiqspaijzwuohbqtolxjysaiayoskijnkgmrppvyspslvvzeemcanvylpgjuxwtw"
"zonjliuxtlyjjhogytdaeiozfamrqpsrirjrgruyfwlonybchhrejhktxewddffddqfesenf"
"rjcujmvbtzgfigqmwhmbwtofsfuududneljnqagnlgzzwwdzfuxyegpdkbeflyidylgajptp"
"nlyukptxhcpafqiphwgbuforjybejzgnnofztniulgdficdbotmnnjthzqxuxzmgoojklsco"
"sjtvktcwiuiifcqvqwpxwjcyliwkfstuxdmztwoaxcmchdewbkhjfonbrcstqnyhtpentvxc"
"dotqqsshurypjzksguektjmtgbonbspsvhsxcrbdzeifogivhrybexhfcupronmirisrafdk"
"nbrnqkrgamfvebykmjeljzrsmuwdlvbojjrarzwalcyxgndcyhfiegglrmmfhxqpwiougyhq"
"najsfkatzdnwyldbghvzknujzjsdsluoyexhnswlmdyjiimbvdqgukxznrampsasojqhdpjs"
"mkicinkojylnaxjumqwvdsmuvupxdpcfjdcebavjcpclkbbgejwnzmyqzbhgxnytmvhjepvk"
"augeofvziekkwhyjhonveoqotuedyhrskyjlcibwltuhssxvxwzrjvaekqkpaksgnkumffot"
"elesbuwfxuyrrziktkuxzycsxyumafpqlnnwdbowjzzombnwnrcaxmpmywmvhnfcqdbgdzgb"
"cxsjfuhnhgegctusleqwtojzvabyluilyyunzmslnbqgjrtwibnvyyzzfbjoqhfaokdkdlps"
"dyigglbvmmvsgikigvdabwupgpdxtykfrvzoxeefuxyptzecpvhbsnkbbelaytkwrstcwczq"
"zbgjbobfaxsybvurphknedlepfuuzkpyzfodmkqdffbwyqnxgxnsthfgwbjibpfjnuoritrt"
"gbkyjrcujgpuoweuobawgzllrrtcauxnyvvrqaacadjhdpfgvuyusfjdawnovfpcalutebuc"
"lttnssqwueylqlkmwnujudawnxtyzbtgonyroppwexmubgeegecbpsafywiniyfoxqyrcwog"
"juslorfzyboiifwrhggfodbuzqvzdxelquloyolmrushxzfiuzdojdjtogpruxpfceekoouz"
"wktmsmfzdcqkyubgasdxatuhbrlnlptmjsafplmlfntrjovrqkugldzvvrelinxvazfkjygn"
"nfchmajqqdynpdkjsmbjysajeqegofqhakrcahngsiswjoixkodyygmumyngnsjuvvbackdk"
"zfbcjzwoeyxengdgxsgkrrpsrrhiigxanriytyjktjoouflfcxerivldvgbasowoawajqxnu"
"mrbhgiaspakmadtuvirwthbvppsgafteztgckcjttxzqfmxfcfumzcagyzexxcbhkyrkmwev"
"qghfjiuopnpcqkjfpceuztzhxsvcdclflkabglwqdfgofrbqbjmunmhivczndkunxapbwwjx"
"ieiwsncvpclvhtwtqiguysqkugmiuollhoixwnsmupcplmrxlqprordkqurhtncllueskayn"
"opaekidvjgfqepjffmfezklllxmkezjwnnloxlvdultvarifopnugajspzypnwsmomdcpouo"
"zmygrppbftzpxipkvklttffcxqqisqfdeeuokphclytdfbtogmmrglfbcbtbhgrjmhyzthid"
"ybwqdywrryzrnfmnuvjuvkdjcwyqwwoaotsmvicodndgxdwwxlkwtbflcnulyjfptodffqvl"
"xjkhvwdoonxanrwjqnbtbvzpsrfrpcrdealcyhjfdqsckbrpyeduwnllelbvrshdeiasmebf"
"hwfiofddqmvnewsapvfgdeqltoreinprmnhrfzvsjkqjgohzpgekjcnzskbwpxkkdsirshoz"
"mpnpvsbmccxebhxlilcubgfwmvislgtzovotufddbuynsmcsefqydbeelnhxpbsdiwyfrnyq"
"zmoyzcewelkxtcohyamcauvvwclzxsgtqnhiuilbqidqmpqxtqskrxtsbixruwhadfpfpvmh"
"phlewrblojkcpdbmqiitviohofbjxzdgfkbotxhzxtahhipvbctlbwypkhkcmkvqkerhbpke"
"fhztyosrkknppcfqbohfuogwxecxpxttbaboidbhacrhevtrmukakzkuqlwtugxhzljwtbvl"
"uaaskjvnpngsicuznwrpbfzhhidraqwenxvcnbnooqpjyqnidypuokvuyqftbnmpvwsenpcv"
"vmnlonxyooiicqzwasbtoasxsmsddczxvknupxtlwoolyjytzzkmfvlzggwosjahjevbaspv"
"eqxqyxuvpprgjifakmostvgqtrrikymrgrameejhvbatmgzuvdeljiipbvgwolhorfxsgram"
"kfpyfvopuxckhvsrhwgdfaauhpmsyqfbsevgwdynhypxhekpfzxxslkbqgclczlxgpvfoxft"
"hrhaqkhqegmxrzsbtmstvcabovuwzsgondounxyrtutjpocrnzwmoctucklqwiyvvnzucemw"
"zwapnmqjmvezkrbeaznhjijfzqyzounzosgcitlyhviyjiedyzxpzbhkojasegsvewoimcoa"
"jhiincnlztekigtcudtdytyxnorzmyghxcpuvljtjghqoqfxirmsistcmsiazlohaflkfawe"
"gkfowlpowpogggdvsrgfkzjlgtxcslqvkdrcpvexvhnuohjdmuqoyvsbyysvbgmvmldqbmcx"
"nutdbftxtiaiihxudsucgzuipmxpyezvhexadlyabrgtukalafiqeczlbihmpbxyerdzsris"
"ulxdfxsnwtolvlynrotowbvjuckrmywqomlxiwvltgvwkdcovvkzebtumcdpwdbwrnflbkqk"
"tnuzjpchwhpxbknfyvqljjqwpfzldyhzlpcuccyllvdaezcrznsbvomriadouenndwyxvclr"
"cjpkoivxmjrwkqrlrijexvxhnpbmwkpvqpbkcqxydrwmpdzykefjjssbtotkvoitduesbfei"
"qfjijwqofledklqmkgssgieplevysqrluzqpavwliosrouzczdyhxhtjtzoudqptlqectrsp"
"hiyevuesqictudybuplshepjkjbtujcpxvobqzzxpgnwwvpenkllotcnlakylegkokkygqoj"
"ivxhnlrpkwmuhcscoyykexlikaouocjgosenadwktjistlbkbjecepgknoljvvdzruwextga"
"aruunbiihinvsc";

const std::string_view kLongPermut =
"uhlqdzjmsmdzrgcjqdevltghvtjzkcckexesbldwjjarkjaocmwubzwqnuqikydqatbvokax"
"tbxakmrobpnuavjzctgjogmnbnjpvlmwlzrxutszuvtkrbxejyklaeqprhhcixtmcnmvvhqh"
"uqjffvmjjycgrgkdrlxkabymcuhesisrqmyumkjqxfeydpbbjflkteblsyscmibgiqovrxpv"
"bejmjaztimulmoclmjwbepasijdlwuvirzxxruoawcipmpbrekogzuctkjobzuhwiefvereu"
"yjbxproizfipceidjaybvymiwpeuiqcatokgdeedufeczbkwcqqocfqqueyofkzjlshjhgkh"
"avgltyzxdhkxddhyddgttfddofoqtmlsykffoffxfhgfcugtegtwvxtkkitogwkcgidpmbck"
"bddialbloyswuntspzwqygllsnczknbtluooxqrzbefgpbldjeowditvnyertifubiuyyuoq"
"kqcpvszrutjmuywyxkbwzfdvodkyzrbthoemktxedeuevzgwstdvfsskqusecqgymzzbohav"
"gvtgrhxvvturrqxwtwgghbpnvftrqsnktgczshbdoabtptehehaoisrwzmbtvpzphzwivxau"
"swemkkgqexxedlzwaxhuhbybnwldcpkbxalpcoymlhqqjyzhwrkukgvyuefvjargjkxnuerb"
"ywamzpbhottksicixcumvtypaogmtxjshajptmpicjmrwmyazqiihiecvufqoqthdmpflydw"
"wcfqrnschgdrciweyfvxcpyebixanzixahhudrtrxtuhvfdyztapcabpfunjmmvhufsdkicq"
"ensiibrfjijvsxjdqzclcaiyoebiatmnmiufbtjnhschoxboojjagijficguwpluyyqosprj"
"ahcqdibeckzbxaezbiglakdwrcnmjanilmudvqivxnifrrbgmpyjfwujupzalhrhptaplxvs"
"uoybzlyoyqdjcpgxmapxftbojsqwnaedfefufvvavpnsghylbqdnomkhbrraikxnmvancqdo"
"ihhtpksiqspaijzwtohbqtolxjysaiaylskijnkgmrppvyspslvvzeemcaniylpgjuxwtwzo"
"njliuxtlyjjhogytdxeihzfamrqpsrirjrgruyfwlonybchhrejhktxewddffddqfesenfrj"
"cujmvbtzgfigqmwhmbwtofsfuududneljnqagnlgzzwwdzfuxyegpdkbefqbidylgajptpnl"
"yukptxhcpafqiphwgbuforjybejzgnnofztniulgdficdbotmnnjthzqxuxzmgoojklscosj"
"fvkucwiuiifclvqwpxwjcyliwkfstuxdmqtwoaxcmchdewbkhjfonbrcstqnyhtpentvxcdo"
"tqbsshurypjzksguektjmtgbonbspsvhsxcrbdzeifogivhrybexhfcuprormirisrafdkcb"
"rnqkrgamfvebykmjeljzrsmuwdlvbojjrarzwalcyxgndcyhfiegglrmmfhxzpwiougyhqna"
"jsfkatzdnwyldbghvzknujzjsdsluoyexhnswlmdyjiimbvdqgukxznrampsasojqhdpjsmk"
"icinaojylnaxjumqwvdsmuvogxdpccjdcebavjcpclkbbpejwnzmyqzbhgxnytmvhjepvkau"
"geofvziekkwhyjhonveuqotuedyhrskyjlnibwltuhssxvxwzrjvaekqkpaksgnkumffotel"
"esbuwfxuyrrziktkuxzycsxyumafpqlnnwdbowjzzombnwnrcaxmpmywmvhnfcqdbgdznbcx"
"sjfehnhgegctusleqwtojzvabyluilyyunzmslnbqgjrtwibnvyyzzfbjoqhfaokdkdlpsdy"
"igglbvmmvsgnkigvdabwupgpdxtykfrvzoxeefuxyptzecpvhbfnkbbeuaytkwrstcwczqzb"
"gjbobfaxsybvurphknedlepfuuzkpyzfodmkqdffbwyqnxgxnsthfgwbjibpfbnuoritrtgb"
"kyjrcujgpuoweuobawgzllrrtcauxnyvvrqaacgdjhdpfgvuyusfjdawnovfpcalutebuclt"
"tnssqwueylqlkmwnujudawnxtyzbtgonyroppwexmubgeegecbpsafywiniyfoxqyrcwogju"
"slorfzyjoiifwrhggsodbuzqvzdxelquloyolmrushxzfiuzdojdjtogprubpfceekoouzwk"
"tmsmfzdcqkyubgasdxatuhbrlnlptmjsafplmlfntrjovrqkugldzvvnelinxvazfkjygnnf"
"chmajqqdynpdkjsmbjysajeqegofqhakrcahngsiswjoitkodyygmumyngnsjuvvbackdkzf"
"bcjzwokyxengdgxsgkrrpsrrhiigxanriytcjktjoouflfcxerivldvgbasowoawajqxnumr"
"bhgiaspakmadtuvirwthbvppsgafteztgckcjttxzqfmxfcfumzcagyzenxcbhkyrkmwevqg"
"hfjioopnpcqkjfpceuztzhxsvcdclflkabglwqdfgofrbqbjmunmhivczndkunxapxwwjxie"
"iwsncvtclvhtwtqiguysqkugmiuollhoixwnsmupcplmrxlqprwrdkqurhtncllueskaynop"
"aekidvjgfqepjffmfezklllxmkezjwnnloxlvdulwvarifopnugajspzypdosmomdcpouozm"
"yirppbftzpxipkvklttffcxqqisqfdeeuokphclytdfbtogmmrglfbcbtbhgrjmhyzthidyb"
"wqdywrryzunfmvuvjuvkdjcwyqwwoaotsmvicodnngxdwwxlkw";

struct ProblemInstance {
  std::string_view text;
  std::string_view permut;
  bool result;
};

const auto kProblemList = std::vector<ProblemInstance>{{"abc", "abcded", false},
{"eidbaooo", "ab", true}, {"eidboaoo", "ab", false}, {"dcda", "adc", true},
{"ooolleoooleh", "hello", false}, {kLongText, kLongPermut, true}};

const auto kApplyProblems = [](SolutionFn&& solution) {
  auto ok{true};

  for (const auto& [text, permut, result] : kProblemList) {
    ok &= (solution(text, permut) == result);
  }

  return ok;
};

bool slow_Solution() {
  return kApplyProblems(slow_IsContains);
}

bool fast_Solution() {
  return kApplyProblems(fast_IsContains);
}

} // namespace

REGISTER_TEST(__FILE__, slow_Solution);
REGISTER_TEST(__FILE__, fast_Solution);
