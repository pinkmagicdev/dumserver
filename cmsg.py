import re
dict = {
	'<f0>' : chr(27) + "\u001b[38;5;0m",
	'<f1>' : chr(27) + "\u001b[38;5;1m",
	'<f2>' : chr(27) + "\u001b[38;5;2m",
	'<f3>' : chr(27) + "\u001b[38;5;3m",
	'<f4>' : chr(27) + "\u001b[38;5;4m",
	'<f5>' : chr(27) + "\u001b[38;5;5m",
	'<f6>' : chr(27) + "\u001b[38;5;6m",
	'<f7>' : chr(27) + "\u001b[38;5;7m",
	'<f8>' : chr(27) + "\u001b[38;5;8m",
	'<f9>' : chr(27) + "\u001b[38;5;9m",
	'<f10>' : chr(27) + "\u001b[38;5;10m",
	'<f11>' : chr(27) + "\u001b[38;5;11m",
	'<f12>' : chr(27) + "\u001b[38;5;12m",
	'<f13>' : chr(27) + "\u001b[38;5;13m",
	'<f14>' : chr(27) + "\u001b[38;5;14m",
	'<f15>' : chr(27) + "\u001b[38;5;15m",
	'<f16>' : chr(27) + "\u001b[38;5;16m",
	'<f17>' : chr(27) + "\u001b[38;5;17m",
	'<f18>' : chr(27) + "\u001b[38;5;18m",
	'<f19>' : chr(27) + "\u001b[38;5;19m",
	'<f20>' : chr(27) + "\u001b[38;5;20m",
	'<f21>' : chr(27) + "\u001b[38;5;21m",
	'<f22>' : chr(27) + "\u001b[38;5;22m",
	'<f23>' : chr(27) + "\u001b[38;5;23m",
	'<f24>' : chr(27) + "\u001b[38;5;24m",
	'<f25>' : chr(27) + "\u001b[38;5;25m",
	'<f26>' : chr(27) + "\u001b[38;5;26m",
	'<f27>' : chr(27) + "\u001b[38;5;27m",
	'<f28>' : chr(27) + "\u001b[38;5;28m",
	'<f29>' : chr(27) + "\u001b[38;5;29m",
	'<f30>' : chr(27) + "\u001b[38;5;30m",
	'<f31>' : chr(27) + "\u001b[38;5;31m",
	'<f32>' : chr(27) + "\u001b[38;5;32m",
	'<f33>' : chr(27) + "\u001b[38;5;33m",
	'<f34>' : chr(27) + "\u001b[38;5;34m",
	'<f35>' : chr(27) + "\u001b[38;5;35m",
	'<f36>' : chr(27) + "\u001b[38;5;36m",
	'<f37>' : chr(27) + "\u001b[38;5;37m",
	'<f38>' : chr(27) + "\u001b[38;5;38m",
	'<f39>' : chr(27) + "\u001b[38;5;39m",
	'<f40>' : chr(27) + "\u001b[38;5;40m",
	'<f41>' : chr(27) + "\u001b[38;5;41m",
	'<f42>' : chr(27) + "\u001b[38;5;42m",
	'<f43>' : chr(27) + "\u001b[38;5;43m",
	'<f44>' : chr(27) + "\u001b[38;5;44m",
	'<f45>' : chr(27) + "\u001b[38;5;45m",
	'<f46>' : chr(27) + "\u001b[38;5;46m",
	'<f47>' : chr(27) + "\u001b[38;5;47m",
	'<f48>' : chr(27) + "\u001b[38;5;48m",
	'<f49>' : chr(27) + "\u001b[38;5;49m",
	'<f50>' : chr(27) + "\u001b[38;5;50m",
	'<f51>' : chr(27) + "\u001b[38;5;51m",
	'<f52>' : chr(27) + "\u001b[38;5;52m",
	'<f53>' : chr(27) + "\u001b[38;5;53m",
	'<f54>' : chr(27) + "\u001b[38;5;54m",
	'<f55>' : chr(27) + "\u001b[38;5;55m",
	'<f56>' : chr(27) + "\u001b[38;5;56m",
	'<f57>' : chr(27) + "\u001b[38;5;57m",
	'<f58>' : chr(27) + "\u001b[38;5;58m",
	'<f59>' : chr(27) + "\u001b[38;5;59m",
	'<f60>' : chr(27) + "\u001b[38;5;60m",
	'<f61>' : chr(27) + "\u001b[38;5;61m",
	'<f62>' : chr(27) + "\u001b[38;5;62m",
	'<f63>' : chr(27) + "\u001b[38;5;63m",
	'<f64>' : chr(27) + "\u001b[38;5;64m",
	'<f65>' : chr(27) + "\u001b[38;5;65m",
	'<f66>' : chr(27) + "\u001b[38;5;66m",
	'<f67>' : chr(27) + "\u001b[38;5;67m",
	'<f68>' : chr(27) + "\u001b[38;5;68m",
	'<f69>' : chr(27) + "\u001b[38;5;69m",
	'<f70>' : chr(27) + "\u001b[38;5;70m",
	'<f71>' : chr(27) + "\u001b[38;5;71m",
	'<f72>' : chr(27) + "\u001b[38;5;72m",
	'<f73>' : chr(27) + "\u001b[38;5;73m",
	'<f74>' : chr(27) + "\u001b[38;5;74m",
	'<f75>' : chr(27) + "\u001b[38;5;75m",
	'<f76>' : chr(27) + "\u001b[38;5;76m",
	'<f77>' : chr(27) + "\u001b[38;5;77m",
	'<f78>' : chr(27) + "\u001b[38;5;78m",
	'<f79>' : chr(27) + "\u001b[38;5;79m",
	'<f80>' : chr(27) + "\u001b[38;5;80m",
	'<f81>' : chr(27) + "\u001b[38;5;81m",
	'<f82>' : chr(27) + "\u001b[38;5;82m",
	'<f83>' : chr(27) + "\u001b[38;5;83m",
	'<f84>' : chr(27) + "\u001b[38;5;84m",
	'<f85>' : chr(27) + "\u001b[38;5;85m",
	'<f86>' : chr(27) + "\u001b[38;5;86m",
	'<f87>' : chr(27) + "\u001b[38;5;87m",
	'<f88>' : chr(27) + "\u001b[38;5;88m",
	'<f89>' : chr(27) + "\u001b[38;5;89m",
	'<f90>' : chr(27) + "\u001b[38;5;90m",
	'<f91>' : chr(27) + "\u001b[38;5;91m",
	'<f92>' : chr(27) + "\u001b[38;5;92m",
	'<f93>' : chr(27) + "\u001b[38;5;93m",
	'<f94>' : chr(27) + "\u001b[38;5;94m",
	'<f95>' : chr(27) + "\u001b[38;5;95m",
	'<f96>' : chr(27) + "\u001b[38;5;96m",
	'<f97>' : chr(27) + "\u001b[38;5;97m",
	'<f98>' : chr(27) + "\u001b[38;5;98m",
	'<f99>' : chr(27) + "\u001b[38;5;99m",
	'<f100>' : chr(27) + "\u001b[38;5;100m",
	'<f101>' : chr(27) + "\u001b[38;5;101m",
	'<f102>' : chr(27) + "\u001b[38;5;102m",
	'<f103>' : chr(27) + "\u001b[38;5;103m",
	'<f104>' : chr(27) + "\u001b[38;5;104m",
	'<f105>' : chr(27) + "\u001b[38;5;105m",
	'<f106>' : chr(27) + "\u001b[38;5;106m",
	'<f107>' : chr(27) + "\u001b[38;5;107m",
	'<f108>' : chr(27) + "\u001b[38;5;108m",
	'<f109>' : chr(27) + "\u001b[38;5;109m",
	'<f110>' : chr(27) + "\u001b[38;5;110m",
	'<f111>' : chr(27) + "\u001b[38;5;111m",
	'<f112>' : chr(27) + "\u001b[38;5;112m",
	'<f113>' : chr(27) + "\u001b[38;5;113m",
	'<f114>' : chr(27) + "\u001b[38;5;114m",
	'<f115>' : chr(27) + "\u001b[38;5;115m",
	'<f116>' : chr(27) + "\u001b[38;5;116m",
	'<f117>' : chr(27) + "\u001b[38;5;117m",
	'<f118>' : chr(27) + "\u001b[38;5;118m",
	'<f119>' : chr(27) + "\u001b[38;5;119m",
	'<f120>' : chr(27) + "\u001b[38;5;120m",
	'<f121>' : chr(27) + "\u001b[38;5;121m",
	'<f122>' : chr(27) + "\u001b[38;5;122m",
	'<f123>' : chr(27) + "\u001b[38;5;123m",
	'<f124>' : chr(27) + "\u001b[38;5;124m",
	'<f125>' : chr(27) + "\u001b[38;5;125m",
	'<f126>' : chr(27) + "\u001b[38;5;126m",
	'<f127>' : chr(27) + "\u001b[38;5;127m",
	'<f128>' : chr(27) + "\u001b[38;5;128m",
	'<f129>' : chr(27) + "\u001b[38;5;129m",
	'<f130>' : chr(27) + "\u001b[38;5;130m",
	'<f131>' : chr(27) + "\u001b[38;5;131m",
	'<f132>' : chr(27) + "\u001b[38;5;132m",
	'<f133>' : chr(27) + "\u001b[38;5;133m",
	'<f134>' : chr(27) + "\u001b[38;5;134m",
	'<f135>' : chr(27) + "\u001b[38;5;135m",
	'<f136>' : chr(27) + "\u001b[38;5;136m",
	'<f137>' : chr(27) + "\u001b[38;5;137m",
	'<f138>' : chr(27) + "\u001b[38;5;138m",
	'<f139>' : chr(27) + "\u001b[38;5;139m",
	'<f140>' : chr(27) + "\u001b[38;5;140m",
	'<f141>' : chr(27) + "\u001b[38;5;141m",
	'<f142>' : chr(27) + "\u001b[38;5;142m",
	'<f143>' : chr(27) + "\u001b[38;5;143m",
	'<f144>' : chr(27) + "\u001b[38;5;144m",
	'<f145>' : chr(27) + "\u001b[38;5;145m",
	'<f146>' : chr(27) + "\u001b[38;5;146m",
	'<f147>' : chr(27) + "\u001b[38;5;147m",
	'<f148>' : chr(27) + "\u001b[38;5;148m",
	'<f149>' : chr(27) + "\u001b[38;5;149m",
	'<f150>' : chr(27) + "\u001b[38;5;150m",
	'<f151>' : chr(27) + "\u001b[38;5;151m",
	'<f152>' : chr(27) + "\u001b[38;5;152m",
	'<f153>' : chr(27) + "\u001b[38;5;153m",
	'<f154>' : chr(27) + "\u001b[38;5;154m",
	'<f155>' : chr(27) + "\u001b[38;5;155m",
	'<f156>' : chr(27) + "\u001b[38;5;156m",
	'<f157>' : chr(27) + "\u001b[38;5;157m",
	'<f158>' : chr(27) + "\u001b[38;5;158m",
	'<f159>' : chr(27) + "\u001b[38;5;159m",
	'<f160>' : chr(27) + "\u001b[38;5;160m",
	'<f161>' : chr(27) + "\u001b[38;5;161m",
	'<f162>' : chr(27) + "\u001b[38;5;162m",
	'<f163>' : chr(27) + "\u001b[38;5;163m",
	'<f164>' : chr(27) + "\u001b[38;5;164m",
	'<f165>' : chr(27) + "\u001b[38;5;165m",
	'<f166>' : chr(27) + "\u001b[38;5;166m",
	'<f167>' : chr(27) + "\u001b[38;5;167m",
	'<f168>' : chr(27) + "\u001b[38;5;168m",
	'<f169>' : chr(27) + "\u001b[38;5;169m",
	'<f170>' : chr(27) + "\u001b[38;5;170m",
	'<f171>' : chr(27) + "\u001b[38;5;171m",
	'<f172>' : chr(27) + "\u001b[38;5;172m",
	'<f173>' : chr(27) + "\u001b[38;5;173m",
	'<f174>' : chr(27) + "\u001b[38;5;174m",
	'<f175>' : chr(27) + "\u001b[38;5;175m",
	'<f176>' : chr(27) + "\u001b[38;5;176m",
	'<f177>' : chr(27) + "\u001b[38;5;177m",
	'<f178>' : chr(27) + "\u001b[38;5;178m",
	'<f179>' : chr(27) + "\u001b[38;5;179m",
	'<f180>' : chr(27) + "\u001b[38;5;180m",
	'<f181>' : chr(27) + "\u001b[38;5;181m",
	'<f182>' : chr(27) + "\u001b[38;5;182m",
	'<f183>' : chr(27) + "\u001b[38;5;183m",
	'<f184>' : chr(27) + "\u001b[38;5;184m",
	'<f185>' : chr(27) + "\u001b[38;5;185m",
	'<f186>' : chr(27) + "\u001b[38;5;186m",
	'<f187>' : chr(27) + "\u001b[38;5;187m",
	'<f188>' : chr(27) + "\u001b[38;5;188m",
	'<f189>' : chr(27) + "\u001b[38;5;189m",
	'<f190>' : chr(27) + "\u001b[38;5;190m",
	'<f191>' : chr(27) + "\u001b[38;5;191m",
	'<f192>' : chr(27) + "\u001b[38;5;192m",
	'<f193>' : chr(27) + "\u001b[38;5;193m",
	'<f194>' : chr(27) + "\u001b[38;5;194m",
	'<f195>' : chr(27) + "\u001b[38;5;195m",
	'<f196>' : chr(27) + "\u001b[38;5;196m",
	'<f197>' : chr(27) + "\u001b[38;5;197m",
	'<f198>' : chr(27) + "\u001b[38;5;198m",
	'<f199>' : chr(27) + "\u001b[38;5;199m",
	'<f200>' : chr(27) + "\u001b[38;5;200m",
	'<f201>' : chr(27) + "\u001b[38;5;201m",
	'<f202>' : chr(27) + "\u001b[38;5;202m",
	'<f203>' : chr(27) + "\u001b[38;5;203m",
	'<f204>' : chr(27) + "\u001b[38;5;204m",
	'<f205>' : chr(27) + "\u001b[38;5;205m",
	'<f206>' : chr(27) + "\u001b[38;5;206m",
	'<f207>' : chr(27) + "\u001b[38;5;207m",
	'<f208>' : chr(27) + "\u001b[38;5;208m",
	'<f209>' : chr(27) + "\u001b[38;5;209m",
	'<f210>' : chr(27) + "\u001b[38;5;210m",
	'<f211>' : chr(27) + "\u001b[38;5;211m",
	'<f212>' : chr(27) + "\u001b[38;5;212m",
	'<f213>' : chr(27) + "\u001b[38;5;213m",
	'<f214>' : chr(27) + "\u001b[38;5;214m",
	'<f215>' : chr(27) + "\u001b[38;5;215m",
	'<f216>' : chr(27) + "\u001b[38;5;216m",
	'<f217>' : chr(27) + "\u001b[38;5;217m",
	'<f218>' : chr(27) + "\u001b[38;5;218m",
	'<f219>' : chr(27) + "\u001b[38;5;219m",
	'<f220>' : chr(27) + "\u001b[38;5;220m",
	'<f221>' : chr(27) + "\u001b[38;5;221m",
	'<f222>' : chr(27) + "\u001b[38;5;222m",
	'<f223>' : chr(27) + "\u001b[38;5;223m",
	'<f224>' : chr(27) + "\u001b[38;5;224m",
	'<f225>' : chr(27) + "\u001b[38;5;225m",
	'<f226>' : chr(27) + "\u001b[38;5;226m",
	'<f227>' : chr(27) + "\u001b[38;5;227m",
	'<f228>' : chr(27) + "\u001b[38;5;228m",
	'<f229>' : chr(27) + "\u001b[38;5;229m",
	'<f230>' : chr(27) + "\u001b[38;5;230m",
	'<f231>' : chr(27) + "\u001b[38;5;231m",
	'<f232>' : chr(27) + "\u001b[38;5;232m",
	'<f233>' : chr(27) + "\u001b[38;5;233m",
	'<f234>' : chr(27) + "\u001b[38;5;234m",
	'<f235>' : chr(27) + "\u001b[38;5;235m",
	'<f236>' : chr(27) + "\u001b[38;5;236m",
	'<f237>' : chr(27) + "\u001b[38;5;237m",
	'<f238>' : chr(27) + "\u001b[38;5;238m",
	'<f239>' : chr(27) + "\u001b[38;5;239m",
	'<f240>' : chr(27) + "\u001b[38;5;240m",
	'<f241>' : chr(27) + "\u001b[38;5;241m",
	'<f242>' : chr(27) + "\u001b[38;5;242m",
	'<f243>' : chr(27) + "\u001b[38;5;243m",
	'<f244>' : chr(27) + "\u001b[38;5;244m",
	'<f245>' : chr(27) + "\u001b[38;5;245m",
	'<f246>' : chr(27) + "\u001b[38;5;246m",
	'<f247>' : chr(27) + "\u001b[38;5;247m",
	'<f248>' : chr(27) + "\u001b[38;5;248m",
	'<f249>' : chr(27) + "\u001b[38;5;249m",
	'<f250>' : chr(27) + "\u001b[38;5;250m",
	'<f251>' : chr(27) + "\u001b[38;5;251m",
	'<f252>' : chr(27) + "\u001b[38;5;252m",
	'<f253>' : chr(27) + "\u001b[38;5;253m",
	'<f254>' : chr(27) + "\u001b[38;5;254m",
	'<f255>' : chr(27) + "\u001b[38;5;255m",
	'<b0>' : chr(27) + "\u001b[48;5;0m",
	'<b1>' : chr(27) + "\u001b[48;5;1m",
	'<b2>' : chr(27) + "\u001b[48;5;2m",
	'<b3>' : chr(27) + "\u001b[48;5;3m",
	'<b4>' : chr(27) + "\u001b[48;5;4m",
	'<b5>' : chr(27) + "\u001b[48;5;5m",
	'<b6>' : chr(27) + "\u001b[48;5;6m",
	'<b7>' : chr(27) + "\u001b[48;5;7m",
	'<b8>' : chr(27) + "\u001b[48;5;8m",
	'<b9>' : chr(27) + "\u001b[48;5;9m",
	'<b10>' : chr(27) + "\u001b[48;5;10m",
	'<b11>' : chr(27) + "\u001b[48;5;11m",
	'<b12>' : chr(27) + "\u001b[48;5;12m",
	'<b13>' : chr(27) + "\u001b[48;5;13m",
	'<b14>' : chr(27) + "\u001b[48;5;14m",
	'<b15>' : chr(27) + "\u001b[48;5;15m",
	'<b16>' : chr(27) + "\u001b[48;5;16m",
	'<b17>' : chr(27) + "\u001b[48;5;17m",
	'<b18>' : chr(27) + "\u001b[48;5;18m",
	'<b19>' : chr(27) + "\u001b[48;5;19m",
	'<b20>' : chr(27) + "\u001b[48;5;20m",
	'<b21>' : chr(27) + "\u001b[48;5;21m",
	'<b22>' : chr(27) + "\u001b[48;5;22m",
	'<b23>' : chr(27) + "\u001b[48;5;23m",
	'<b24>' : chr(27) + "\u001b[48;5;24m",
	'<b25>' : chr(27) + "\u001b[48;5;25m",
	'<b26>' : chr(27) + "\u001b[48;5;26m",
	'<b27>' : chr(27) + "\u001b[48;5;27m",
	'<b28>' : chr(27) + "\u001b[48;5;28m",
	'<b29>' : chr(27) + "\u001b[48;5;29m",
	'<b30>' : chr(27) + "\u001b[48;5;30m",
	'<b31>' : chr(27) + "\u001b[48;5;31m",
	'<b32>' : chr(27) + "\u001b[48;5;32m",
	'<b33>' : chr(27) + "\u001b[48;5;33m",
	'<b34>' : chr(27) + "\u001b[48;5;34m",
	'<b35>' : chr(27) + "\u001b[48;5;35m",
	'<b36>' : chr(27) + "\u001b[48;5;36m",
	'<b37>' : chr(27) + "\u001b[48;5;37m",
	'<b38>' : chr(27) + "\u001b[48;5;38m",
	'<b39>' : chr(27) + "\u001b[48;5;39m",
	'<b40>' : chr(27) + "\u001b[48;5;40m",
	'<b41>' : chr(27) + "\u001b[48;5;41m",
	'<b42>' : chr(27) + "\u001b[48;5;42m",
	'<b43>' : chr(27) + "\u001b[48;5;43m",
	'<b44>' : chr(27) + "\u001b[48;5;44m",
	'<b45>' : chr(27) + "\u001b[48;5;45m",
	'<b46>' : chr(27) + "\u001b[48;5;46m",
	'<b47>' : chr(27) + "\u001b[48;5;47m",
	'<b48>' : chr(27) + "\u001b[48;5;48m",
	'<b49>' : chr(27) + "\u001b[48;5;49m",
	'<b50>' : chr(27) + "\u001b[48;5;50m",
	'<b51>' : chr(27) + "\u001b[48;5;51m",
	'<b52>' : chr(27) + "\u001b[48;5;52m",
	'<b53>' : chr(27) + "\u001b[48;5;53m",
	'<b54>' : chr(27) + "\u001b[48;5;54m",
	'<b55>' : chr(27) + "\u001b[48;5;55m",
	'<b56>' : chr(27) + "\u001b[48;5;56m",
	'<b57>' : chr(27) + "\u001b[48;5;57m",
	'<b58>' : chr(27) + "\u001b[48;5;58m",
	'<b59>' : chr(27) + "\u001b[48;5;59m",
	'<b60>' : chr(27) + "\u001b[48;5;60m",
	'<b61>' : chr(27) + "\u001b[48;5;61m",
	'<b62>' : chr(27) + "\u001b[48;5;62m",
	'<b63>' : chr(27) + "\u001b[48;5;63m",
	'<b64>' : chr(27) + "\u001b[48;5;64m",
	'<b65>' : chr(27) + "\u001b[48;5;65m",
	'<b66>' : chr(27) + "\u001b[48;5;66m",
	'<b67>' : chr(27) + "\u001b[48;5;67m",
	'<b68>' : chr(27) + "\u001b[48;5;68m",
	'<b69>' : chr(27) + "\u001b[48;5;69m",
	'<b70>' : chr(27) + "\u001b[48;5;70m",
	'<b71>' : chr(27) + "\u001b[48;5;71m",
	'<b72>' : chr(27) + "\u001b[48;5;72m",
	'<b73>' : chr(27) + "\u001b[48;5;73m",
	'<b74>' : chr(27) + "\u001b[48;5;74m",
	'<b75>' : chr(27) + "\u001b[48;5;75m",
	'<b76>' : chr(27) + "\u001b[48;5;76m",
	'<b77>' : chr(27) + "\u001b[48;5;77m",
	'<b78>' : chr(27) + "\u001b[48;5;78m",
	'<b79>' : chr(27) + "\u001b[48;5;79m",
	'<b80>' : chr(27) + "\u001b[48;5;80m",
	'<b81>' : chr(27) + "\u001b[48;5;81m",
	'<b82>' : chr(27) + "\u001b[48;5;82m",
	'<b83>' : chr(27) + "\u001b[48;5;83m",
	'<b84>' : chr(27) + "\u001b[48;5;84m",
	'<b85>' : chr(27) + "\u001b[48;5;85m",
	'<b86>' : chr(27) + "\u001b[48;5;86m",
	'<b87>' : chr(27) + "\u001b[48;5;87m",
	'<b88>' : chr(27) + "\u001b[48;5;88m",
	'<b89>' : chr(27) + "\u001b[48;5;89m",
	'<b90>' : chr(27) + "\u001b[48;5;90m",
	'<b91>' : chr(27) + "\u001b[48;5;91m",
	'<b92>' : chr(27) + "\u001b[48;5;92m",
	'<b93>' : chr(27) + "\u001b[48;5;93m",
	'<b94>' : chr(27) + "\u001b[48;5;94m",
	'<b95>' : chr(27) + "\u001b[48;5;95m",
	'<b96>' : chr(27) + "\u001b[48;5;96m",
	'<b97>' : chr(27) + "\u001b[48;5;97m",
	'<b98>' : chr(27) + "\u001b[48;5;98m",
	'<b99>' : chr(27) + "\u001b[48;5;99m",
	'<b100>' : chr(27) + "\u001b[48;5;100m",
	'<b101>' : chr(27) + "\u001b[48;5;101m",
	'<b102>' : chr(27) + "\u001b[48;5;102m",
	'<b103>' : chr(27) + "\u001b[48;5;103m",
	'<b104>' : chr(27) + "\u001b[48;5;104m",
	'<b105>' : chr(27) + "\u001b[48;5;105m",
	'<b106>' : chr(27) + "\u001b[48;5;106m",
	'<b107>' : chr(27) + "\u001b[48;5;107m",
	'<b108>' : chr(27) + "\u001b[48;5;108m",
	'<b109>' : chr(27) + "\u001b[48;5;109m",
	'<b110>' : chr(27) + "\u001b[48;5;110m",
	'<b111>' : chr(27) + "\u001b[48;5;111m",
	'<b112>' : chr(27) + "\u001b[48;5;112m",
	'<b113>' : chr(27) + "\u001b[48;5;113m",
	'<b114>' : chr(27) + "\u001b[48;5;114m",
	'<b115>' : chr(27) + "\u001b[48;5;115m",
	'<b116>' : chr(27) + "\u001b[48;5;116m",
	'<b117>' : chr(27) + "\u001b[48;5;117m",
	'<b118>' : chr(27) + "\u001b[48;5;118m",
	'<b119>' : chr(27) + "\u001b[48;5;119m",
	'<b120>' : chr(27) + "\u001b[48;5;120m",
	'<b121>' : chr(27) + "\u001b[48;5;121m",
	'<b122>' : chr(27) + "\u001b[48;5;122m",
	'<b123>' : chr(27) + "\u001b[48;5;123m",
	'<b124>' : chr(27) + "\u001b[48;5;124m",
	'<b125>' : chr(27) + "\u001b[48;5;125m",
	'<b126>' : chr(27) + "\u001b[48;5;126m",
	'<b127>' : chr(27) + "\u001b[48;5;127m",
	'<b128>' : chr(27) + "\u001b[48;5;128m",
	'<b129>' : chr(27) + "\u001b[48;5;129m",
	'<b130>' : chr(27) + "\u001b[48;5;130m",
	'<b131>' : chr(27) + "\u001b[48;5;131m",
	'<b132>' : chr(27) + "\u001b[48;5;132m",
	'<b133>' : chr(27) + "\u001b[48;5;133m",
	'<b134>' : chr(27) + "\u001b[48;5;134m",
	'<b135>' : chr(27) + "\u001b[48;5;135m",
	'<b136>' : chr(27) + "\u001b[48;5;136m",
	'<b137>' : chr(27) + "\u001b[48;5;137m",
	'<b138>' : chr(27) + "\u001b[48;5;138m",
	'<b139>' : chr(27) + "\u001b[48;5;139m",
	'<b140>' : chr(27) + "\u001b[48;5;140m",
	'<b141>' : chr(27) + "\u001b[48;5;141m",
	'<b142>' : chr(27) + "\u001b[48;5;142m",
	'<b143>' : chr(27) + "\u001b[48;5;143m",
	'<b144>' : chr(27) + "\u001b[48;5;144m",
	'<b145>' : chr(27) + "\u001b[48;5;145m",
	'<b146>' : chr(27) + "\u001b[48;5;146m",
	'<b147>' : chr(27) + "\u001b[48;5;147m",
	'<b148>' : chr(27) + "\u001b[48;5;148m",
	'<b149>' : chr(27) + "\u001b[48;5;149m",
	'<b150>' : chr(27) + "\u001b[48;5;150m",
	'<b151>' : chr(27) + "\u001b[48;5;151m",
	'<b152>' : chr(27) + "\u001b[48;5;152m",
	'<b153>' : chr(27) + "\u001b[48;5;153m",
	'<b154>' : chr(27) + "\u001b[48;5;154m",
	'<b155>' : chr(27) + "\u001b[48;5;155m",
	'<b156>' : chr(27) + "\u001b[48;5;156m",
	'<b157>' : chr(27) + "\u001b[48;5;157m",
	'<b158>' : chr(27) + "\u001b[48;5;158m",
	'<b159>' : chr(27) + "\u001b[48;5;159m",
	'<b160>' : chr(27) + "\u001b[48;5;160m",
	'<b161>' : chr(27) + "\u001b[48;5;161m",
	'<b162>' : chr(27) + "\u001b[48;5;162m",
	'<b163>' : chr(27) + "\u001b[48;5;163m",
	'<b164>' : chr(27) + "\u001b[48;5;164m",
	'<b165>' : chr(27) + "\u001b[48;5;165m",
	'<b166>' : chr(27) + "\u001b[48;5;166m",
	'<b167>' : chr(27) + "\u001b[48;5;167m",
	'<b168>' : chr(27) + "\u001b[48;5;168m",
	'<b169>' : chr(27) + "\u001b[48;5;169m",
	'<b170>' : chr(27) + "\u001b[48;5;170m",
	'<b171>' : chr(27) + "\u001b[48;5;171m",
	'<b172>' : chr(27) + "\u001b[48;5;172m",
	'<b173>' : chr(27) + "\u001b[48;5;173m",
	'<b174>' : chr(27) + "\u001b[48;5;174m",
	'<b175>' : chr(27) + "\u001b[48;5;175m",
	'<b176>' : chr(27) + "\u001b[48;5;176m",
	'<b177>' : chr(27) + "\u001b[48;5;177m",
	'<b178>' : chr(27) + "\u001b[48;5;178m",
	'<b179>' : chr(27) + "\u001b[48;5;179m",
	'<b180>' : chr(27) + "\u001b[48;5;180m",
	'<b181>' : chr(27) + "\u001b[48;5;181m",
	'<b182>' : chr(27) + "\u001b[48;5;182m",
	'<b183>' : chr(27) + "\u001b[48;5;183m",
	'<b184>' : chr(27) + "\u001b[48;5;184m",
	'<b185>' : chr(27) + "\u001b[48;5;185m",
	'<b186>' : chr(27) + "\u001b[48;5;186m",
	'<b187>' : chr(27) + "\u001b[48;5;187m",
	'<b188>' : chr(27) + "\u001b[48;5;188m",
	'<b189>' : chr(27) + "\u001b[48;5;189m",
	'<b190>' : chr(27) + "\u001b[48;5;190m",
	'<b191>' : chr(27) + "\u001b[48;5;191m",
	'<b192>' : chr(27) + "\u001b[48;5;192m",
	'<b193>' : chr(27) + "\u001b[48;5;193m",
	'<b194>' : chr(27) + "\u001b[48;5;194m",
	'<b195>' : chr(27) + "\u001b[48;5;195m",
	'<b196>' : chr(27) + "\u001b[48;5;196m",
	'<b197>' : chr(27) + "\u001b[48;5;197m",
	'<b198>' : chr(27) + "\u001b[48;5;198m",
	'<b199>' : chr(27) + "\u001b[48;5;199m",
	'<b200>' : chr(27) + "\u001b[48;5;200m",
	'<b201>' : chr(27) + "\u001b[48;5;201m",
	'<b202>' : chr(27) + "\u001b[48;5;202m",
	'<b203>' : chr(27) + "\u001b[48;5;203m",
	'<b204>' : chr(27) + "\u001b[48;5;204m",
	'<b205>' : chr(27) + "\u001b[48;5;205m",
	'<b206>' : chr(27) + "\u001b[48;5;206m",
	'<b207>' : chr(27) + "\u001b[48;5;207m",
	'<b208>' : chr(27) + "\u001b[48;5;208m",
	'<b209>' : chr(27) + "\u001b[48;5;209m",
	'<b210>' : chr(27) + "\u001b[48;5;210m",
	'<b211>' : chr(27) + "\u001b[48;5;211m",
	'<b212>' : chr(27) + "\u001b[48;5;212m",
	'<b213>' : chr(27) + "\u001b[48;5;213m",
	'<b214>' : chr(27) + "\u001b[48;5;214m",
	'<b215>' : chr(27) + "\u001b[48;5;215m",
	'<b216>' : chr(27) + "\u001b[48;5;216m",
	'<b217>' : chr(27) + "\u001b[48;5;217m",
	'<b218>' : chr(27) + "\u001b[48;5;218m",
	'<b219>' : chr(27) + "\u001b[48;5;219m",
	'<b220>' : chr(27) + "\u001b[48;5;220m",
	'<b221>' : chr(27) + "\u001b[48;5;221m",
	'<b222>' : chr(27) + "\u001b[48;5;222m",
	'<b223>' : chr(27) + "\u001b[48;5;223m",
	'<b224>' : chr(27) + "\u001b[48;5;224m",
	'<b225>' : chr(27) + "\u001b[48;5;225m",
	'<b226>' : chr(27) + "\u001b[48;5;226m",
	'<b227>' : chr(27) + "\u001b[48;5;227m",
	'<b228>' : chr(27) + "\u001b[48;5;228m",
	'<b229>' : chr(27) + "\u001b[48;5;229m",
	'<b230>' : chr(27) + "\u001b[48;5;230m",
	'<b231>' : chr(27) + "\u001b[48;5;231m",
	'<b232>' : chr(27) + "\u001b[48;5;232m",
	'<b233>' : chr(27) + "\u001b[48;5;233m",
	'<b234>' : chr(27) + "\u001b[48;5;234m",
	'<b235>' : chr(27) + "\u001b[48;5;235m",
	'<b236>' : chr(27) + "\u001b[48;5;236m",
	'<b237>' : chr(27) + "\u001b[48;5;237m",
	'<b238>' : chr(27) + "\u001b[48;5;238m",
	'<b239>' : chr(27) + "\u001b[48;5;239m",
	'<b240>' : chr(27) + "\u001b[48;5;240m",
	'<b241>' : chr(27) + "\u001b[48;5;241m",
	'<b242>' : chr(27) + "\u001b[48;5;242m",
	'<b243>' : chr(27) + "\u001b[48;5;243m",
	'<b244>' : chr(27) + "\u001b[48;5;244m",
	'<b245>' : chr(27) + "\u001b[48;5;245m",
	'<b246>' : chr(27) + "\u001b[48;5;246m",
	'<b247>' : chr(27) + "\u001b[48;5;247m",
	'<b248>' : chr(27) + "\u001b[48;5;248m",
	'<b249>' : chr(27) + "\u001b[48;5;249m",
	'<b250>' : chr(27) + "\u001b[48;5;250m",
	'<b251>' : chr(27) + "\u001b[48;5;251m",
	'<b252>' : chr(27) + "\u001b[48;5;252m",
	'<b253>' : chr(27) + "\u001b[48;5;253m",
	'<b254>' : chr(27) + "\u001b[48;5;254m",
	'<b255>' : chr(27) + "\u001b[48;5;255m",
	'<u>' : chr(27) + "\u001b[4m",
	'<b>' : chr(27) + "\u001b[1m",
	'<r>' : chr(27) + "\u001b[0m"
}
 
# Create a regular expression from the dictionary keys
pattern = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))
def cmsg(text):
	# For each match, look-up corresponding value in dictionary
	return pattern.sub(lambda mo: dict[mo.string[mo.start() : mo.end()]], text) + "\u001b[0m"
