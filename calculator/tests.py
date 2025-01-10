from django.test import TestCase, Client
from unittest.mock import patch
from calculator.models import FuelPrice
from calculator.utils import load_fuel_data, calculate_fuel_stops

class LoadFuelDataTests(TestCase):
    @patch("calculator.utils.load_fuel_data")
    def test_load_fuel_data(self, mock_load_fuel_data):
        # Mock external API call for loading fuel data
        mock_load_fuel_data.return_value = None

        # Ensure that fuel data is loaded without errors
        load_fuel_data()
        self.assertTrue(mock_load_fuel_data.called)

class CalculateFuelStopsTests(TestCase):
    def setUp(self):
        # Create FuelPrice objects with real data
        FuelPrice.objects.create(
            opis_truckstop_id=1,
            truckstop_name="Shell Gas Station",
            address="123 Broadway Ave",
            city="New York",
            state="NY",
            rack_id=101,
            retail_price=3.899999
        )
        FuelPrice.objects.create(
            opis_truckstop_id=2,
            truckstop_name="Chevron Gas Station",
            address="456 Sunset Blvd",
            city="Los Angeles",
            state="CA",
            rack_id=102,
            retail_price=4.250000
        )
        FuelPrice.objects.create(
            opis_truckstop_id=3,
            truckstop_name="BP Gas Station",
            address="789 Lakeshore Dr",
            city="Chicago",
            state="IL",
            rack_id=103,
            retail_price=3.750000
        )
        FuelPrice.objects.create(
            opis_truckstop_id=4,
            truckstop_name="ExxonMobil",
            address="101 Main St",
            city="Houston",
            state="TX",
            rack_id=104,
            retail_price=3.490000
        )

    def test_calculate_fuel_stops(self):
        route = {
            "geocoded_waypoints":
            [
                {
                    "geocoder_status": "OK",
                    "place_id": "ChIJIQBpAG2ahYAR_6128GcTUEo",
                    "types":
                    [
                        "locality",
                        "political"
                    ]
                },
                {
                    "geocoder_status": "OK",
                    "place_id": "ChIJE9on3F3HwoAR9AhGJW_fL-I",
                    "types":
                    [
                        "locality",
                        "political"
                    ]
                }
            ],
            "routes":
            [
                {
                    "bounds":
                    {
                        "northeast":
                        {
                            "lat": 37.8273051,
                            "lng": -118.228056
                        },
                        "southwest":
                        {
                            "lat": 34.0549009,
                            "lng": -122.4193154
                        }
                    },
                    "copyrights": "Map data ©2024 Google",
                    "legs":
                    [
                        {
                            "distance":
                            {
                                "text": "383 mi",
                                "value": 615965
                            },
                            "duration":
                            {
                                "text": "5 hours 49 mins",
                                "value": 20969
                            },
                            "end_address": "Los Angeles, CA, USA",
                            "end_location":
                            {
                                "lat": 34.0549009,
                                "lng": -118.242651
                            },
                            "start_address": "San Francisco, CA, USA",
                            "start_location":
                            {
                                "lat": 37.7749452,
                                "lng": -122.4193154
                            },
                            "steps":
                            [
                                {
                                    "distance":
                                    {
                                        "text": "0.4 mi",
                                        "value": 650
                                    },
                                    "duration":
                                    {
                                        "text": "3 mins",
                                        "value": 153
                                    },
                                    "end_location":
                                    {
                                        "lat": 37.769282,
                                        "lng": -122.4178934
                                    },
                                    "html_instructions": "Head <b>south</b> on <b>S Van Ness Ave</b> toward <b>12th St</b>",
                                    "polyline":
                                    {
                                        "points": "m|peFv_ejVTEd@KPCVGdB_@n@OXG`@KbASn@M@AbAUREHC`@GBAfB_@TEr@Oj@MHANEd@SFEPKLIJGBCD?@AJ@P@j@DB?B@J@`@DL@B?B@p@BP?"
                                    },
                                    "start_location":
                                    {
                                        "lat": 37.7749452,
                                        "lng": -122.4193154
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance":
                                    {
                                        "text": "0.2 mi",
                                        "value": 345
                                    },
                                    "duration":
                                    {
                                        "text": "1 min",
                                        "value": 36
                                    },
                                    "end_location":
                                    {
                                        "lat": 37.7696405,
                                        "lng": -122.4170737
                                    },
                                    "html_instructions": "Slight <b>right</b> onto the <b>US-101 S</b> ramp to <b>I-80 E</b>/<wbr/><b>Oakland</b>/<wbr/><b>San Jose</b>",
                                    "maneuver": "ramp-right",
                                    "polyline":
                                    {
                                        "points": "_yoeFxvdjVJHFDFBHDB@BBDDDFBFBFBHBF@H?H@H?F?@?HAHAFAHCFCHCFEDEFEDEDEBMDG@I@G?GAKAIEGCGGEECCAAEIEKAICKAMAQ?Q@Q@UBc@Dc@?AFu@F_A?A?AKW"
                                    },
                                    "start_location":
                                    {
                                        "lat": 37.769282,
                                        "lng": -122.4178934
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance":
                                    {
                                        "text": "0.4 mi",
                                        "value": 692
                                    },
                                    "duration":
                                    {
                                        "text": "1 min",
                                        "value": 35
                                    },
                                    "end_location":
                                    {
                                        "lat": 37.7690767,
                                        "lng": -122.4092574
                                    },
                                    "html_instructions": "Continue onto <b>US-101 S</b>/<wbr/><b>Central Fwy</b>",
                                    "polyline":
                                    {
                                        "points": "g{oeFtqdjVB]Be@B]?K?K@Y@g@@q@?a@@e@BeB?y@@g@@_A?y@@s@?Y@[Am@?s@BkA?O?g@D_CD{@Dq@H_APcBFk@BY@KPmB"
                                    },
                                    "start_location":
                                    {
                                        "lat": 37.7696405,
                                        "lng": -122.4170737
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance":
                                    {
                                        "text": "7.5 mi",
                                        "value": 12108
                                    },
                                    "duration":
                                    {
                                        "text": "8 mins",
                                        "value": 489
                                    },
                                    "end_location":
                                    {
                                        "lat": 37.8253948,
                                        "lng": -122.3038929
                                    },
                                    "html_instructions": "Take the exit onto <b>I-80 E</b> toward <b>Bay Brg</b>/<wbr/><b>Oakland</b>",
                                    "maneuver": "ramp",
                                    "polyline":
                                    {
                                        "points": "wwoeFz`cjVBWBU@GBY@UBWBYB_@@W@K@[@_@@Y?C@]@_@?]@c@?E?W?Y?MA_@Ce@CUAICUACACGUCGKSCEEGEEEGA?IIIIOGGCCAKEICKAKAKAYAg@BUBM@MDWHUFUJKDSAe@VIDUNEBGDULSLOHIDA@SJ]NIDIBKBODWHYFOBYBQ@K@I@K?I?G?I?I?M?W?C?UAOCKAKAOAICOCUGQGEAOEQISGOGQIYOOGOKSKUOMIYSWSECMKSQIISSQOYYKKKKW[QUQWQYQYOUKQGOMW[s@GMSe@EIWm@KWKUIUWm@Ym@M[M[O]IOWo@MYEMWg@CEEIGMAAOWIMMQOWQS?AKMCEMQMQU]W[Y_@[_@o@u@U[a@g@UYe@m@e@k@s@{@s@{@aBsBaBqBUYUW[_@IKKOUWm@u@QSU]GIGIU[MM?A[a@[e@U[MOU[SUOSKMIIGIGGCECECECCEECECECCCECECCAECCCEEECECEACUa@a@q@OYS_@CG?ACECGCGEGCGCGCGCGCEEICGCEEMGKEKEKYi@Wc@MUWg@KOGMGKGIGIKQIKUYKMcAiAIKGGa@e@q@u@s@u@SUUUAAe@i@iAmAs@w@UWo@s@s@w@SWSUAAi@i@IKc@g@yA}AAAy@{@uCcDA?cAiAg@k@][k@o@k@o@u@}@u@y@c@c@kAqAYY[[e@i@o@s@k@o@OQKKOQQSUSaAeAIIY[Y[y@_AUWWWEE[]o@s@kAqAe@g@q@u@Y[UUSUiAoAm@s@]]yCcDm@q@aDmDOQ[]EESSSU_AcAs@u@k@m@c@i@CC[[EGQSCCGGQSGGw@}@oAuAAAk@m@OO]a@i@k@eBkBMOIIEEIK[]sByBsB}BwBaCw@{@iAmA_CeCmAuAk@o@y@}@k@m@oAyAaAeAKOMMs@w@s@w@CAs@w@QSEESUIIQQ_@a@_@a@_@_@_@_@[[CCKKUWII[[KKUWYWq@s@KM]]KMWa@MSU[e@m@SY]g@[c@ACGIQWOUWe@OUIKS]IOIM[o@IOSc@Sa@O]Q]ISEIe@cAGKOYGOKUa@{@GMEIIOQ_@Qa@ACc@}@Ug@Wg@IQYo@[m@O_@Q]Yk@Wk@]q@_@y@KUu@}Am@qAUg@Sg@Ws@KWOc@YeAq@_CMi@Kk@Kc@I_@CQAEKo@Ga@EWIo@COCSCQCQAQCUCSCSAUEa@KyAMyAOmBKmAGs@Ca@Ek@Gu@SgCGs@Gu@KoAAUEi@CUGw@Gu@AMASMyAGs@QaCCUGu@IeAGo@KwAKmAEq@Ea@ASE_@Ca@CYGs@Ca@SkCE]IgAEk@C]E_@AUCSIeAAWI{@Gq@OqBGs@AMEk@?AGk@?EAKEe@C_@CSCa@CSC[CYCa@AMI_AI{@C[AMG{@Eo@Em@Ea@GcAK_BE}@G{@G}@GoAMaCEiAAYCm@Cm@C_@CaACaAEsACe@Ag@AMAg@Ci@C_AGgBCg@Ac@A[AUAYCYA_@Ce@Cg@Cc@Es@Co@Ec@C_@Eu@Gy@Eg@I_AMuAEi@?AIs@K_AEc@SwBWgCIy@E[Iw@Ea@O{AQkBSmBy@eIWiCKeA[{CWmCw@eHKiBUqDEe@?EAOGu@Ca@C_@AWCg@AMAOA_@Cc@C_@AYCc@C_@AYC_@Ca@Cc@Ce@CQAMAWCQC]C]Gg@Gc@EWAMEa@CGIs@?CG_@M}@?E]cC"
                                    },
                                    "start_location":
                                    {
                                        "lat": 37.7690767,
                                        "lng": -122.4092574
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance":
                                    {
                                        "text": "0.9 mi",
                                        "value": 1369
                                    },
                                    "duration":
                                    {
                                        "text": "1 min",
                                        "value": 52
                                    },
                                    "end_location":
                                    {
                                        "lat": 37.826323,
                                        "lng": -122.2890607
                                    },
                                    "html_instructions": "Take exit <b>8B</b> for <b>I-580 E</b> toward <b>Oakland</b>/<wbr/><b>US-24</b>",
                                    "maneuver": "ramp-right",
                                    "polyline":
                                    {
                                        "points": "uwzeFhnniVJe@Ku@C[E]Gi@C[Ge@Ec@CWAGC]E]Ea@E_@CWGg@E[I{@EYIw@Ec@Ge@MaACOCOC[AGAEE[E_@EWCSIq@G]CWAIGc@E[K}@M}@Km@Ic@G]I_@GQCGI_@CIEQKYK_@IYQk@I[EMESGWCIAMCKAICK?ECOCOAOAGAK?KAGAK?KAI?KAK?I?UAc@?I?I?O@[@I?K@K?I@K@QFe@?CHg@BSBI@KDOFW?AFSFUPi@HSPe@HWFOFOBMFODQBKH]H[H[@GDQBI@EBM@I@I@EBOBS@I@K@I@I@K?I@E?C@K?I@I@K?G?C?I@U@I"
                                    },
                                    "start_location":
                                    {
                                        "lat": 37.8253948,
                                        "lng": -122.3038929
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance":
                                    {
                                        "text": "45.3 mi",
                                        "value": 72937
                                    },
                                    "duration":
                                    {
                                        "text": "42 mins",
                                        "value": 2494
                                    },
                                    "end_location":
                                    {
                                        "lat": 37.7417528,
                                        "lng": -121.5738944
                                    },
                                    "html_instructions": "Continue onto <b>I-580 E</b>",
                                    "polyline":
                                    {
                                        "points": "o}zeFrqkiV?S@M?UAo@Ak@Aa@Ce@Cm@M_ACSO{AK{@AOCQGg@O{AIo@CWE[Gm@E]AMQ{AIy@K{@AMGo@Gc@AGAQC[A]Cc@?C?]AW?Y?Y@]@e@@a@@GBo@BWBO@QD[BQ@IJo@Js@BU@IHi@Ls@Ho@TuA?C\\_CRqA@GD]LaAL{@F]Fi@Hk@@GHk@BQHi@N}@@MF[ZsBBO@EHi@Jq@F]Fa@BSJm@RmAFi@D]D]DW?CTyA@G^_CDYD[Fc@BK`@oCD]PcABQPkARqANeAFa@@GBQBQ?A@C?CBODY?ABOF]BS@EDY@G@KBKDW@IFa@Jo@Fc@Ha@L}@L}@Fc@BODYBUBKB[BQB[Fg@DWBSHu@P{AJy@`@sCHm@PmAHc@h@sCNq@Je@@GLc@FU@CDQJa@@EHYBEDSL_@DMFSBKDOHWDOL_@BGDMXy@HWJUJ[Nc@FOL[JYN]^{@BIHOXo@JYFKFMJUN[NYFOFMLWNWHODKNWNWFOFIPYLWP[NUNYDGHMR[PYNS@CPUPUNUPUFIRUZ]RUTURSRQFGLKRORQJGJIVQBANKRMl@]TKJGRIXMNEXMj@SXKVEREBAVEXGVEhAUB?DAPEZEREHCPCXG@?REXGp@MXEPE\\G^IDA`AQHAPELCLCLCFA`@If@KHCHCJCPGHEJETKHEDCJERMHGBAFEBCDCHIHGBCNOFEFGJKDGHKFIRWJODEJQHMFKDKJSHSRe@L]FQDMHUHe@FYDYH_@?CF[DUJg@Ly@H]Lu@DSBQDSBQFYF]Ha@Fa@H_@BQBOH_@F_@Ha@BO@KFYDWLo@Lu@Lq@H_@DYPy@Lq@BKJ[BOBK@EHYDUBER{@HWH]Pm@\\iABIRo@HUBGJ[@CXw@J[Vq@Z{@BGHSJ[FQNa@L[@C@CHWL[@CFSZ{@L[Nc@Rk@Pg@JWNc@`@eA@GTo@Zu@Xu@L[L[LYDGVm@\\s@HODINYLYXe@T_@\\i@^o@DKFIRYFIDILQDIT[PUPWd@m@BA`@i@JOh@u@t@cAT[NQPWDE^i@PUb@m@PU?ANUPWNWNYNWN[JUL[L[N]HWHURq@DODKFUH]F]BMDQF]F[@IDWBS@MD[Fk@DUFg@@I@MBQ@IJ}@F_@D_@d@wDBYDUD]Dc@Hi@BYNiA\\uC\\iC`@gDHk@L}@ViBPqANaAD]Fa@Lo@Hi@DWHg@D[F_@Js@@EPeADUBSHi@Ha@?CPeARoA?AHc@F_@F_@Ls@BODYD[F[D[DQ@IF_@@KDUF[F_@D]@AJo@@IF_@?CF_@Ha@?ALw@DU@KBOBQBK@IF]H]F_@H]FY@EH]H[Ja@HU@CLc@FSNc@L]J[L[HWVo@J[b@kAFSJWRi@L]Rk@^gAL[Vs@@AL]JY^eANa@Rk@HSP_@N[JWJQRa@LWLUR]JOBEFKLSJODGV_@PWDG@?\\c@RUHKHI@ATWRUDCRSTURQ^]fAcADCv@s@h@g@\\[z@u@h@e@HIj@i@RQLMDENMFGTSRSTWBA`@c@PSPSNSZc@PWPU\\i@JOR]P[R]FMVe@LWTi@Ti@Pa@^cALYn@cB\\}@JUr@gBl@yAVq@FMJWPg@P_@Tk@DMHU^_ARi@Tm@DKJYL]L_@DOTu@@GBE@EH[DQFSHYV{@BQDKFYH_@Ha@Nq@@GHa@@IDSP{@@GLy@@IDWF_@Fa@B[R}AFk@Hq@Be@HaAHeABg@Bc@HaBBe@DqA@e@@k@?Y@e@?[@e@?I?U@cA@K?S?M@cADyD@U?Y@a@?]@q@@q@@oA@aBBwC@e@@{@@a@?YBeA?S@O?G@_@B]@[D_@?CBYD_@BK@IFa@DUBMH]Li@FQHY@CJ[J]L[JU@ENYNYNY^s@FIR_@@CTc@HMf@_ALQ~@eBZi@DKFKHORa@HOVi@b@_AFOLUJWd@aAFMJUh@oAXs@FQFMTi@Tk@P_@`@aAPc@~@yBtAaD\\y@FOLYVo@@AFMJYFMDML[FQDKL[L[BGHSHWFOb@mAPg@@ELa@FOZ}@DMDKFO|@iCJY|@iCNe@Xw@@CBIL[Pe@?ABIDIFOL[J[L[L[L]FKDML[L[N[L[L]BGBGDIL[L[L[L[L[LYJUDKDIDMJYFMFMHUPa@L[L]BEHSLYL]FMNa@LWDKJWN]HSFOh@gADIHONYLWFMHMR_@DEDI@AJSNSDGFKJOJQT[LQHMHKJMFINQ@CDENQj@q@NQNORUVWRSPQXUJKNMLMVQJIFGTQTQNK\\UHGb@YHGFCNI^UXQBADCn@]NGLIJENILG`@U@?HEJGHEd@UZQRKZOVONIHEHELGFEZORKJGTMVMTMVM`@SPKNIFCDCHEdAq@TOZSBCHGRMJKLITSJGLKRQROJIHGLKRONO^WPOFGVQLINMFEPMFETOZSHGJGTOXQl@_@z@g@FCDCTMPKJGJINIPKb@UDC^U`@UXQb@WXOZONINGNGBADCLEXMb@OXKHCFCPEVIZINCHCFABAHAHALCd@Gh@ED?NAZAn@@\\?J@P@TB\\BPBD@F@LBZFJBLBXHNFHBNFB?FBFDHBHDFBTJ\\TFBRNPJTPVRRPPRJJHHFFPPb@f@HJBBBBhAnAFHFD\\`@`@d@PPJLZZTRVRTRHDHFNJDBJFTLVLNHHBVJVJLDRFNDZHVDB@D?PDNBJ@XDT@J@J?P@V@Z?X?NAXAVATCTADALCZEDAZG`@KTGHCPGLGRGLGPGFCNGHCXMXKd@QZMVKJENGVITKPG\\MFCPIl@Ub@QJEVKXKVKHCd@Sn@ULGRIh@SVKb@OJE\\ODCFCNGVM@ATKJGPKHGRMLIFGTOPOBAXW@ALMLKZ[PSJKDGFIJMTY?APUPWNWPWLShAgBJQV_@LST]JM@AX_@PUPQLMFGLMPQRQTQHINKb@[LIf@_@RMHGDCNId@]ZUBA~@o@LKTO^WPONMFGFGDEJK\\_@PQZa@NQNSBGLODGDGJODEz@iAFKr@_ADGBE\\e@RWRWBCBCBCBETWJKFENOHIPMTQFGBCFEVO\\SBATOf@UTINGd@QTGVIZG\\GTEh@IDA^Ef@Id@GZE`AMDAREJA\\G|@MTCZGXCHCPC`@Gz@M@?z@MXGVCJCDADAZG^GjAUVElB_@HAjAUXGZGLCbASHAPEn@KFCNAl@M~@ONCNA`@GXEFAPCJA`AINAh@EZCHAZCvAMFAD?|@Il@EXCVC\\Ef@ITEHAh@MPEJC\\KXI@?HEh@Qd@Sh@U`@UZQ`@W^Ud@]NKHGTONKh@_@NMFEh@_@r@g@JIDENI^Yl@a@@APMh@_@HGBAFGp@a@d@[BA^WTMJGf@YLI\\Sh@YBCl@Yr@_@FCx@a@JERKDAd@UTKf@Sp@YPGPIf@QDAFCHEf@Qz@YTIXKJELEXKl@UVIt@WRId@Of@S^Qp@[HEz@e@`@W\\S\\W^Wb@]\\YDEv@s@VWb@e@V[d@i@X_@LQFIDIRWPYLSLSHMDIDIFKJSDIFMR_@FMN]LWN[N_@JYN_@J]HQ`@kABETq@DMJWBGBGJYVo@@C@EDKDILYJSLYDKLUNYBGJQDIHMNYPWDGBE@AT]LS\\g@fAyAFKRWp@_AHKT[j@y@FILQBCFKh@s@f@q@JOJOLQJOHOLUNWBGHQDIDGBIP_@FMHWFMNc@BIJYL]La@To@Tq@Ts@Rk@L]FQ@GVu@@A^cAVq@L_@N]L[JWRc@JWPa@DI^y@Pa@DIRc@Xk@JSFKFMZm@JSBEjAyB@Cj@gAPYBIHMFKfAuBd@{@Zm@R_@HMLUfAuBT_@d@_AZk@BCDIh@cAHQFIf@_Ab@{@FK\\m@Xc@@AP[Za@^g@DGV]\\_@TYHI\\]NOVWTS^]f@c@f@c@LM^[p@k@JIHIRQ`@]TSp@m@VUh@a@NO`A}@`@]ZYJIl@m@HGNMDEHITSrAkATSf@a@~AwAr@m@TUBAHIZYZWl@i@VUv@s@`@]NKRQTS`@_@z@s@JMPMPQVYPSTWHKHMDEX_@P[Xa@R]JSN[JQFOFORc@Na@LYFUPg@DSFQDODSDODOFWBQFWDYHa@DYFc@Fm@NiBDs@Bo@?O@G?wA?O?eAAc@Cu@?KCUEy@AOM_BAg@GgACs@AEKgCCm@AMAa@GoAAc@CYAe@Og@?u@?w@Ac@?k@?_@?g@As@?kAA]?[?I?m@?m@?C?uA?k@?}AA}A?qA?eCAqA?sB?Q?m@?a@?YAq@?uAAoD?i@Ak@?i@?mA@w@?qA?IAcA?s@?Y?Q?E?Q?[?]?O?]?{AAcC?c@?[AgB?W?cA?S?u@?g@Aq@?g@?}@A{C?qAAw@?A?m@?{AA_A?UAu@Ag@Am@AM?IC{@?AGuBIiBGiAAUAMEi@Ei@AUMmAAQIo@Gg@Iu@Ec@G]Ik@CQGi@OmACMG]Ic@Ic@Ow@i@wCGYOw@EW[gB[aBQcAESGYEQCMIa@s@}Da@wBKk@Ia@G]Oy@Ii@Ko@?CI]CWGc@Ee@I}@Go@E}@Ey@C}@Cw@AO?g@Au@@q@?}@@a@?CBs@@e@@[HwAFu@Dy@LsB?KLeC@QDgA@g@?s@?{A?_@?c@?AA[Ao@AYC]?IAQCc@AOAMCa@CWIeAE_@E_@E]Ga@G_@E[G_@I_@G_@I_@Qs@?AESGSAGEMK]I]Ma@M_@Oa@?AM_@MY?ASe@O_@?A[q@[m@CIMUS_@OWYe@S_@]e@?AOQOSY_@OQACOQs@y@c@e@AAc@e@UWUWeBmBKM_AcA_AeAwA}AiCuC]_@m@u@GKW]OUQWKQOWEGKSOYQ]KQIQGMIQKUQa@Qc@Sk@IUMc@Oc@K]IYK_@I[ACCKGWG[Ka@?CG]G[G]Ic@AMKu@Ga@CYE_@E_@AQC_@?GCUAQEm@Co@ASAc@Cc@?_@Ao@@S?_A?q@?S@a@@S?I@QBm@Bc@Be@@SBSB[@IBa@D]Hy@BK?ABWRmATmABQJg@@EJm@RgA@GBMF_@Ha@@GDWBK@G@GBOJq@@G@MJ{@B]Hy@B_@Bm@B_@BS@]@a@@a@@W@a@@m@?U?i@?[A{@Ae@Ak@Aa@AYCe@C[C_@C_@C_@E_@C]CQGi@Ga@CWEUE_@ESGa@G[I_@EQWmAIYEQ[mAK[CMK[CKK_@I]Y_AMg@K]EUESKa@Ke@G_@CQAGKk@CMAKCSEUGi@Gc@Ee@E_@C_@C]AYEg@?C?CAYCc@?UCaACs@EuBAy@GsDA{@EyBAe@?KCi@As@EwBEyB?c@EwBCy@?c@EcBCoACoAE_CAcAGuD?MEcCG}BCuBCm@Ay@CwA?UCcC?k@@_CFkCB}A@OHuBBc@LuBBUBe@Fo@?CRgBDYD_@D_@L_A?EPkAD[Hg@BKJm@Jk@Hc@F]Jo@Nk@Ni@Rs@H[Ni@DSJ_@DOFQBMJ_@Pk@JYHYL]HWXy@L]Pi@Ng@Rk@J[L[L_@J]La@L]J[J[J[J]?ANe@Lg@Ry@H]Ha@Nq@DYJe@F]@IBQBOBQD_@Da@D]D_@Da@B_@B_@B_@@MB]Bc@Bu@@W@[B_@B_@Ba@Ba@Ba@B_@@a@B_@Ba@B]B_@?E@U@EBa@Ba@B]B_@Da@B_@D_@B_@Da@B_@D_@HaAD]r@iHFo@Fo@BQNeB@IPeBFk@Fk@Dk@Fk@BUBWVcCDm@Fk@Fk@Fk@`@aEJcABa@D_@D_@@K@SD_@Ba@B_@B_@B[@CBa@B]DcAB_@B_@Ba@@_@Bu@Bg@@Y@K@_@@a@@_@@a@?_@@_@DsC?Q?a@?a@@_A?O?q@A_@?a@?c@A_AC_BA_@?c@A_@A_@AU?ICa@?ICu@A_@Ca@A_@Cc@C]Cc@A[Ca@IcAC_@C_@Ca@E_@Ca@E_@C_@E]CUAKI}@KaAE_@Ea@E]I_AEa@E]QeBIy@Ec@E_@E]AQAQC]C_@?AC_@C_@Aa@A]Cc@?YAg@A_A?_@?c@?aA@m@?o@@_E?mA@}D?uB@yCBuW@cEAaA?c@@wD?m@?m@?k@BiL?_@@eE@eE@sE?O?]?O@iA?iB?_@@sD?O?m@@a@?a@?gA?m@Ag@?y@AU?OA_@?a@Cc@Aa@Ac@Ae@Eq@Eu@MsAC[Go@Eg@Gg@Io@Io@QkAGe@Kk@G_@CUAGCOG_@CSIe@c@wCa@uCOmAG_@EYCSGe@Ga@Ge@EUQuAKs@Ge@AEKw@CMKu@SwAEUEYw@gFKo@Gc@E]G]E]AGEUE]G_@E]U_BOgAAIE]OgAMy@E_@EYE[S}AG]Gk@Iu@E_@EYC[CUQgCKoBE_A?g@Aw@Cs@?gA@kC@eB@aC@g@?_A@u@?iA@sA?qA?y@?u@BwBBoB?G?Q@k@?M?O?C@a@?EB_C?Y@]?_@?c@@[?]?i@?Y@}@?I@_D@mB@aB@oA@gB@eC?]@kB@{A?s@@{ABqD?U@kA?y@?G@{A?i@@s@@yF?m@@gB?C?eA@m@?m@?oB?w@?c@?G?qA?yA?eA?i@?cA?qA?cA?K?[?i@?m@?g@@i@?eH?K?M?aC@aD?o@?a@?a@?S@]?e@?_D@qC?_@?]?kA?{@?mA?{@?_A@iB?iCAiD?gC?qD?gB?gB?uB?}A?m@?eC?o@?aC@qF?q@AmBA}FB_GBsD?sA?a@@u@?iB@kA?G@uF?W?w@?Y@yA?m@@uD@uF@gD?qB@mE@yE@mD@aE@sEBwFBkE@{C?m@?c@AcA@{D?yB?gC?k@?a@?a@?c@?_@?K?W?a@?e@?_@?a@?a@@eA?a@?O?Y?w@?eA?oA?i@?wA@c@?a@?c@?y@?k@@c@?_@?_@?]?kA@c@?a@?a@?c@?a@?K@w@?a@?c@?c@@a@?a@?Y?i@?a@?U@S?{@?c@?c@@cA?a@?c@?a@?e@?c@@]?Q?q@?a@?c@?c@@cA?W?I?gB?a@?a@@o@?U?a@?a@?a@?a@@c@?a@?_@?c@?c@?a@?Q?O@a@?c@?a@?a@?c@?e@@]?a@?a@?[?E?c@?_@@c@?c@?Q?M?c@?a@?I?W@eA?]?M?a@?i@?_@?S?]@W?yA?k@?S?W?I?a@?K@U?c@?a@?a@?_@?c@?a@@c@?a@?Q?s@?_@?c@@_@?c@?_@?e@?a@?Q?O@a@?c@?a@?a@?eA?a@@a@?{A?K?a@?a@?c@?a@@a@?c@?[?E?_@?c@?a@@eA?a@?a@?c@?a@?a@?a@@c@?[?Y?M?a@?c@?a@?a@@c@?iA?[?c@?cA@_A?mB?a@?a@@a@?c@?_@@oE?mC@cB?a@?C?C?[?K?S?c@?a@@gB?a@?a@?c@?g@?Y?A@a@?c@?a@?]?M?Y?M?S@gB?c@?S?M@gB?a@?U?M?cA?c@@}@?mA?y@@oA?[?yD@S?uA?qA@o@?{@@mFFi\\BcG?m@?gB@aA?mD@uB?k@@_A@eF?]?e@?G?u@?c@?a@?U@K?g@@a@Bc@@[B[?IB]B[@IBU@IDW@I@MBOL_ATcBTaBLcAb@cDTcBF_@Da@Fa@F_@Da@Da@Ba@Da@Ba@Ba@Ba@@a@Ba@@a@@a@?a@@c@?c@?a@?a@Aa@AeAAa@Ca@Aa@AQAOA_@Cc@EsAASCo@Ew@Aa@KeCYsHKgCMiCMoDEw@Cs@Cm@A]Eu@G_BEcAEcAA]Ci@C]Aa@Cc@C_@GeAEa@G_AIgAC_@Ea@Ea@Ca@KcAEa@UeCC_@a@kEg@mFY}CU}Ba@oEQkBa@mEYuCMsAWoCCYIcAKaAIaAEa@Gs@AKAIKoACi@AGG_AC_@Ce@Aa@Ew@Co@Ca@A]Cw@Co@Aa@Ac@?Q?OA[?EEsA?{A?_@?a@?a@@a@?c@?a@?a@?a@?_A?A@cB@a@@y@@s@@i@FaDBqBD_C?ADcC@_A@y@FaDJoG@m@@_AHcFHaF@i@@cA@k@DoB?E?S@G?QBgBBeB@c@@_@@eB@{A?U?_@Aa@?_@?AAa@?G?UAc@A_@Ac@Ac@AO?QCc@Aa@ACA]Cc@Ca@Ee@CYEc@M_BGc@Ec@Ea@AGE[E[G_@E[ACGa@G]Ia@CQMo@I_@Ke@Q{@I_@CEG[I[IYAEK]e@}A}@sCMc@_@gASo@q@wBOa@EQAAMc@[_AY}@Y}@EMQi@[aACK]gAUs@Qg@Y}@e@wAY}@e@{AY}@KYK]Ma@c@sAiB{FGQGOEQGQGOEQGQGQcAaD?Ac@sAq@uBm@kBQi@]gAe@yAOe@Us@g@}AIY_@iAa@mAYaAM_@Uw@M]K_@Oe@CI]aAOc@IWs@yBI[u@_Cg@_B}BkH[_AMc@Ww@a@oA[eAY{@[_ACISm@So@Oe@K]CIQk@M]a@oA[_Ac@oAGQ]eAWw@[aAs@yBe@uAgAcDs@{Bg@yAq@_C_@wAKc@Mg@K_@Ia@CKGSKg@Ms@Q{@Mw@ESCUKk@E[Gg@c@aDg@aEm@wEGc@E_@CQCQUsBS_BCSGa@Is@OgACUKu@MgAc@gDAMQ{AM{@Gi@MaA?CIq@e@mDc@uDi@iEQyAE]]iC]yCM{@g@iEM}@CWG_@Ea@AKCQEY?CCMCUE_@G_@AGQwAE]COCOGa@G_@G_@AMCMCQCOG]G]?AG_@G_@G]G]E_@I_@Ga@?CEYI_@E_@G]AIEUIg@ESCOE[CMCSGc@Ga@E[CWAQAOCUC_@C_@ASAO?MAQ?SCcA?A?Q?K?K?W@k@DaBBe@@_@JeBDgA@QNyCFeA@UDy@B_@@SDo@Di@Hw@D_@Fa@Hi@@CHg@Ja@DUH]FUNi@La@Nc@J[JWBGN_@Pa@HOHOLW`@s@Ta@JOR[PYR_@^m@LSj@gALWRe@FMHUL]JUNc@FSHWHU?CFSFS@EJc@Pw@BIBQDSBMDWJm@BQBYBUFe@Da@B_@D_@?CB]Bg@@W@_@?QBg@?[?o@?]?Y?a@A]Ac@ASAUA]Eg@C[AWAKEa@Gg@?AE[E[CQIk@G]CKCOIc@Kg@AGG]Ki@AIEQOy@EQEUCOScAKi@Oy@EWCKGa@G[EQCKQ{@Mw@_@sBMo@UoAACKm@Oy@Kg@GWCQCMG[Ic@GUKi@CMCGScAOs@S}@Om@Qw@Kg@]yAUgAk@gCq@{CI[Ic@GYOm@Qu@Ia@AIGUESGUIa@K_@S_AI]?AI]Ka@G[I_@GYK_@CQEMI_@Qw@ScAGUI[Ke@G[I[UaA[yAKc@UaAGYCKGW[kAMi@I]I]I]I[Ia@IYS_A_@{A?Ee@qBQu@S{@AGK_@ESGUCQMe@a@iBAGKc@U}@Qu@AGGYIYI]AGUaACMQq@Ia@AAI_@ESMi@I]EUCII_@Sy@S{@Ke@I[I]CMEOKa@Mi@ESI]Ka@AIEMKe@K]Ma@M]GSEKOc@O]EISe@?AIQ[i@S]GIIMW_@e@m@UYSUc@a@IIMMGEGGa@[GGKISMc@]]U[UWSIEYU[U_@YOMKIKIUSQOCCWWSQUUSUUWKKMMc@i@SWIKGISYQWSYIKEIS[QYEK]k@OYEIGKQ[O[GQIMEKGOGMEMO]M]GOCIM_@I[K]I[I_@Ke@G_@Ia@G_@E_@Ea@Ec@E_@Ca@Cc@Ca@A_@Ae@A]Aa@Aa@Ae@Aa@Aa@A_@Ac@A_@Ac@A_@EiAA]Ac@Aa@Ac@A_@Ac@Aa@Cc@Aa@Aa@Aa@Ac@?AC[Ac@Ac@Aa@Ac@Ca@A_@Aa@Ac@Ca@Aa@A_@Ac@Aa@Ce@A]Aa@Aa@?AAc@A[ACCeAAa@Aa@Ca@A_@Ac@Ac@A_@Cc@Aa@Ac@Aa@Aa@AIAYAa@A_@Aa@Ac@Cc@A_@Aa@Ac@Ca@?SAMAc@Ac@AUAKAa@A_@Cc@Ca@EcAAWAKC_@Cc@C]Cc@Ea@AMAUC_@Ec@E_@Ca@Ea@E_@Ee@E_@E_@Gc@E_@Ea@Ga@E]Gc@Ga@G_@E_@Gc@GYGc@Ga@Ic@AAO}@E[ACG_@I]Ga@Ia@G_@I_@G_@I_@G_@Ia@Ia@G]G_@CKESIa@G_@Ia@G]G_@I_@G_@G[ACIe@G_@I_@G]I_@Ga@Ia@G]I_@G_@Ia@G]Ic@G_@G]EUAMG_@G_@G]Gc@E]Ga@Gc@E]Ga@E_@Ea@Ga@E_@Ec@Ea@E_@Gc@Ea@E_@E_@Ec@Ea@E_@E]CWCMEa@CWAGEa@Gc@C_@Gc@E_@Ea@E]?CE]Ec@CWAGKaAGc@CUAKK}@?CE_@E_@CUAMEa@E_@AGCOAIK}@?EAGCWGc@E_@CYAIE]Ga@Ea@E_@COAOGc@Ec@E]Ea@MaAE_@Ec@E_@Ec@E_@Ga@E_@Ec@Ea@E]Ea@AMKw@E_@E_@Ea@Ec@E[C]AEK_ACSCSC_@E_@Iq@Gm@QyAQkBGk@E[CWKgAQyBASSeCEi@Eg@?ECW?GGs@C_@CUAMC_@C[AGC_@Cc@ACC[AOAQCY?EEe@G_AGeACa@?MCSAc@Ca@C_@Ce@Aa@C_@CcAEeAEcACeAEaACeAEaAAc@EcACm@Ae@Cy@"
                                    },
                                    "start_location":
                                    {
                                        "lat": 37.826323,
                                        "lng": -122.2890607
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance":
                                    {
                                        "text": "16.9 mi",
                                        "value": 27219
                                    },
                                    "duration":
                                    {
                                        "text": "15 mins",
                                        "value": 874
                                    },
                                    "end_location":
                                    {
                                        "lat": 37.5909837,
                                        "lng": -121.3339934
                                    },
                                    "html_instructions": "Slight <b>right</b> to stay on <b>I-580 E</b> (signs for <b>Interstate 580</b>/<wbr/><b>Interstate 5 S</b>/<wbr/><b>Fresno</b>/<wbr/><b>Los Angeles</b>)",
                                    "maneuver": "turn-slight-right",
                                    "polyline":
                                    {
                                        "points": "}ljeFx{_eVJY?A?AASE_EA}@CgA?a@A_AAm@Am@CkACwBAy@?_A?E@cABcA@cA@O@S@Y?GBa@?A@_@FaAH}@?KFk@?KD_@Bc@HcA@U@IBc@HcAHcAHcADu@Fo@FeAHcAHcADg@Ba@HgAJaAFc@@KJs@PaANw@VkAV}@V}@J]X}@Zy@Zy@N[N]NYZm@BGR]HQb@u@T[FKJOPWd@o@@?\\g@RUZc@HKRWRUPSLQDEPWRUPWRUPWRUPURWPUPURUd@m@PUd@m@f@m@PSRYPURUPWf@m@d@k@jAyAz@aAPUNOV[RUd@i@RUPUTUd@k@f@k@nAwAd@k@`@c@RUNS@An@s@PURURSPUZ_@HIPSTW?Az@aAFG^c@RSRWj@q@HIVYd@k@RUTW~AgBdAoAZ]tDgErA}ANSHIBEFGLODEt@}@hHiIh@m@`BkBxEqF`BmBj@o@`AgAr@y@r@y@TY\\_@l@q@|AkBZ_@X]RWRWRUPWRWRWNSRYRUPWPWPWPWHKFKNURYPWNWPYNSPYNWPYPYNYNULUR]JSHMR]d@{@HQFKNY^q@Ra@NYDKJSFMNWN[NYNWN[LWJSDGLYLS@ENYNWN]NYHODGN[BGJON]LUFMFMP]LU`@w@NYLYNYNYP[NYLWN[NYP[NYLYNYNYBEFKBEN[?ALUP[DIFMNYNYBEJUNWN]DGHOBGHQNWN[P[DKFKNYBIP]@ARa@b@w@DMLSNYN[NYLWP[NYN[FKHQ`@q@P[NYLYPYNYLYLYNYP[z@gBLYNYNWJSBELYBCJSP]LWP]NWHOFMLUDIHQNYN[NYDIJQLYNYNYDIJQLYLUFKJULSHQFKLWN[DGHOJSBGNYNYN[NYNYN[LWPYN[BEHOJSBGNYP[JWR]LWNY\\q@N[PYNYHQBGN[FKTc@`@w@NYN[^q@LYP[NYNYNYN]LUP[N[^s@NYN[NYLWP[HQDIP[LULYNYN[NYNYP[JUNYR_@LWNYLYPYLWNYN[BGJON]NWP]LWLWBELUNYP]LWN[LWP[HQFILWRc@HMN[NYLWNYP[LYPYNYN]NYNWBGJSNYLW`@u@NYLYP[NYLUTe@JUJON]PYN]NWNYN[P[LWP]NYLYPYLYNWLW@CNYP[FMFKLYNWN[NYN[NWN[JSBENY@CLULWLYR]P]LUHQZm@Te@R]|@gB\\q@P[LWLWBGLWNWBEXm@P[`@u@LYN[NYDITc@R]@ELSP]LYPYLWHQHQJQBGFMR]LWP[NY^u@N[p@oA^u@\\o@N[LWP[LYXg@JSVi@P[LWNYNYLYPYN]NWNYNYN[N[NWN]NWN[LUNYNYN[NWN[NYN[DGHQPYN[LWNYP]LWNYN[N[LUN]P[LWP]LUNYNYNYLWP]NYP[NYLWPYLYP[LWP[LYP[LWN[PYLW@ALYNYNYLWP[LWP]NWL[P[NYNYNYN[NWN[NYN[LWBCLUN[LYNWP]NYLYNYDIHMN[LWPYN[NYNYBGHQNYP[DIHODIHON[NWLYNWN[NYNYN[NYLUP_@NWN[NYFMFKNYN[NYNYLWNYN[PYN[LWNYP[LWN[NYNYDGHQDIHOJSBELYP[NWN[LWN[PYN[LWFKFMLU@CN[NYNYLWBCLWNYHQDGP]LWNYN[NWNYFMHOJS@AN[LWNYNYP]LWNYNYP[LWN[NYNY@CLUN[P[NYJUR_@NYLUN[NYLWP[N[JSBEN[NWLYP[LW^s@`B_D`@w@JSDIN[DGDKNWN[j@gATc@BGFK`AmB^s@^u@NYNY^s@N[LW^u@P[\\s@NYPYNYJUf@eAz@_Bn@mAJUZm@Xg@N[DGDKP[LWNYJSR_@NYNYLWRa@LURa@HOTc@Zk@N[LWp@qAVe@BGn@oAr@sA`@w@Zo@Xk@FMZm@@AVe@d@_AVe@HQTc@Zk@HSP[LUNYDIHQDGTc@Rc@NYNYN[P[LUN[LUP_@NWHQBEP]DGHQDIHOJS@CP[N[Ra@x@}ANYP]LWP[N[JSR_@N[NWN[NYNYNYLYNYNYNWN]LULWR_@LUHQR_@N[NYNYNYN[NWN[LYHMVg@N[DIHONY^q@NYNY^s@FMVe@DIHOn@oAJUp@oA^s@?APY^u@NYl@oAP[Tc@FO\\o@^u@^u@DGHQNYNYN[FIFOLSP_@BCJUHOTc@NY^u@NY^s@\\s@NYNYNYNYDIHODKDGN[b@y@N[v@yAvAuCLUn@oAnBuDl@kATc@Xk@p@qA^u@Tc@Vg@NYVe@j@gAHQ@AN[LWP[NYTc@HO?ANWLYNYNYNYHODIN[NYNW^u@^s@N[n@mALW^u@NYVe@FMN[b@y@JSNWnAcCN[\\o@^u@nAcC`@s@LYVg@@CDIXi@Tc@P]JQn@oAb@y@Zm@LW^u@Tc@HO~@iBTc@JSj@gA?A^s@HQDINY^s@NYN[^q@bAoBNYZk@R_@LYR]JS^s@N[PYBGt@wAP_@R_@t@}ATc@JSn@qAP]NYNY`@u@z@aBRa@NYZm@HQBGP]Tc@dAoBb@y@R]LWNYP]Zi@BE^u@Xk@Pc@LS^w@`@y@z@_B`@w@^s@nDcHLUBEZo@n@mAd@{@Xm@NW^u@\\q@Xi@DI\\q@R_@^u@l@kA^s@^s@P]LWl@kAJSVe@Vg@FMJQN[NYv@{ALUj@gAj@gAFMLUFOb@w@P_@NYPYLYFKFMNYP]LWNYLWP[@ALWNYNYNYN[NYJS@CNYNYNYN[NWN]FIHOLUN]NYHMRa@P]NYLYNYNWLWBELW^s@JUPYHS@ATe@NWNYLW@CNWLYFKHOLWP[LYFKDI@CNWDIHQHOrB}DN[r@sAN[P]P]DGTc@DKNWBEP_@DIXg@P]NYLYP[NYNYNYNYN]NWJSBELWP[N[LUDIHQDGHQP[LYNYFIFOLU@AN[NWLWN[NYP[JSBENYNYNYLYNYNYNYNYNYNYNYLYBELUFMFKLW@ANYNYNYLYNYNYN[NYNYNYNYNYNYNYNYNYN[NYNYLWNYNYN[NWLYP[NWN]Zk@Ra@HON[LUN[P]n@oAl@mA`AiBl@mA`AgBXm@HMHQj@gAXi@@At@yAJSDKl@iA?AP[^s@`@s@LWR]NWDIHOLUP[@A^o@P[Ta@HMBGLQP[LSR[NW`@o@LS@Cn@cAJMZg@LSDGLSBCNUFKHMZc@b@o@FIZe@FIhA_Bb@o@FIHKn@}@Xc@PUNURYNULOJQX_@V]fA}ABEpAiB|@oAZc@FKRWV]FKt@eAV_@HKv@gA|@qANUHKX_@DILODGn@_A`@k@x@iAnAgBZc@JOV_@vCeEPWZc@`@k@~@sArAkBb@o@PWRYh@u@^i@vAqBd@o@PWRYh@w@PUnAgB\\g@bAuAbAwAnBsCNSBEbBaCDGRWHMFKPUPWRW?ALSTYLSNQBEBEPWNSRYV_@rBsCT]|@oAHMRYPU@C@AJODG`@i@HMDGHKFIb@o@NU@ARYRYPU`@m@HIHMV]JOd@q@NUPWt@cARYPW`@k@PWHKFKPWPWPULQDGPWLQ@Cb@m@HMh@u@RYRWDIPWLQPSZg@HK^g@d@s@d@m@`AwAXa@`CgD`@k@PWT]LQRWPW@?\\i@z@kAXa@Ze@NQ@CPWDGLOPWPWLQDE~A}BHMd@o@@A@CBEHKDGBCFId@q@NURYb@m@PU?ARWNWPUd@o@DIJMV_@l@{@^i@BCHKFKLQ@CBCFKV]@Cn@}@HIDIBCFIT]BEHKDG@ABCz@oAHKHKJQBERYPUHMDET]PUT]JMFKNSf@q@v@iA"
                                    },
                                    "start_location":
                                    {
                                        "lat": 37.7417528,
                                        "lng": -121.5738944
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance":
                                    {
                                        "text": "308 mi",
                                        "value": 495350
                                    },
                                    "duration":
                                    {
                                        "text": "4 hours 35 mins",
                                        "value": 16485
                                    },
                                    "end_location":
                                    {
                                        "lat": 34.08807609999999,
                                        "lng": -118.2359573
                                    },
                                    "html_instructions": "Merge onto <b>I-5 S</b>",
                                    "maneuver": "merge",
                                    "polyline":
                                    {
                                        "points": "s~ldFl`qcVh@w@t@cANUHKZe@NSNU@?RYHKDGRYNU@ANUJODGPUFKJMPWJOFG\\g@|@oAPWPW@APWRWNUPWPWPWPWRWRYNURYHKl@y@PWd@q@b@m@JODGRYDEHMPWd@q@JMFKNUPUPWPWRWPWRWNUPWNURWPWb@m@R[b@m@NSNQBEPYRYr@_ADIRWNUBG`@i@PUPWPYPUPUPWT[PWPUPYPURYPUPWPWFIHORWPWDGJMPWPWRYPWb@o@RWNWHKHKPUPWPWRYNURYNSz@mA^i@TYFIXc@TYPW\\g@DGRWPWDGHMRYPWRWPYPUNSDILQPWRWb@o@PUPWNUT[PURYb@o@FIFIRYd@q@PUNUT[PWNSf@q@@CNUPURYPWPUJQRYBCPWd@o@NURWPWRYFIHOPSR[NURW@CJM@CPURYPWRWNWRWPWRWPWNU@APUPWRYPWb@o@LOBELQDGNUPWRWPYPURWPYRWNUv@gAPWHK|@qAnBoCt@eA`@k@HMj@w@RYJQ\\c@NUFIT[V_@b@o@h@s@JO\\g@\\g@V]bAwAJO`@k@l@y@RY@C`@k@DGHKRYLS@?JQRW`@k@PWPWRYHMDGf@s@^g@RY@CPUV_@T[JOTYPWXa@?ARWd@o@PWPULSRYBCLSRYLODIPWHKHMDEJMf@u@JONUPUJODGBCLSd@m@LSDENUPW`@k@RW@CRYNSRYp@cABCNURUR[LQRYFI\\g@NUPSPWFIHMf@s@LSRWPW@ALQRYPWPUT]LQd@q@PUDG@AHKLSBEn@{@V_@RYHKFKRY^i@TYLSFILQRYNSR[PSb@m@?ARYPWNSPWBE`@k@RWNURWNWPUPWRWNULQV]V_@NUDEpIwLPUp@_AlAeBXa@PWnBoCNURYPUPWPWPWPURYRYNU`@i@T]PWPUt@gADELQPUPWRYNURYPU@C`@k@RYNST[PWBELQPUNURWb@o@PW@ANURW\\e@Xc@NSd@o@PYRWNURWRYPWJQ@ARYRWV_@PULSLQFIFKT[HKFKPURYRWPWPU@CPUNWPWPURYPUPUPYBCNSFKHKd@q@PUPWPWPUPWPWPUb@o@LQV_@JMNUHIPYd@o@PWPUPWHMFKPUXa@HKT[NURWPWDGHMTYT[PYJOXa@JMPWd@q@V]HKLS@APWJM\\g@RYt@eAPWRWPWRYPUPWBCn@}@V_@LQr@cA^i@T[DG`@k@BCHMHMPUBEDGRWRYNURWNWPUDGJMLSX_@BEJMPWNULSLQ`@i@Xa@DILQJOLONUb@m@j@y@JOXa@HKPWRYPUPWPUNULSDET[HKBEHKHKBG@C\\e@tCaEt@gABCNSNURYTYLSRW@ANUPURWPWRUPWBCNURUPUPUPWRWd@k@PUFIJMRWPUf@m@PURWRWf@m@b@k@@APUPSRWPUv@_ADGFGFI@CPSJKFKPURURURWRWd@m@RUPWRURUPURURYNS`BqB~AqBX]NQPSPUTYPURUPURWPURUPUTWPUPURWRWRUPUPUPU@?RWPS@CPSRWPURURWRUPWPSTYZ_@HKRWjA{APURWBCNQRYTWRWNQPSPURUNSTWRWd@k@RWRW~D_Fd@m@PURURWRUPUf@o@DGjB_C~AoBDG~BuCtBiC^e@pA_Bx@cAd@m@RUd@m@f@m@hAwABELOlAyAd@m@TWNSb@k@@ARUDGPSRWLQBAb@k@BCPUPS@ANSBENORW?APSRUTYNSRUPW@APSRWRWRUPWf@k@v@cAf@o@RUHKFGRYd@k@zAiBBGPSf@o@RWRUpBeCrBgCf@o@PSRWx@eAVYFGV]RUFILQPUp@y@|@gAT[RUf@o@p@y@TWT[BCnBaCRYjAyARUd@m@PSRWTWb@k@TWRWb@k@RURWf@o@PWPSRYPSPWRWRWb@m@PWTW`@k@RYPUDIZc@T[PW`@m@d@q@b@o@`@o@RYNU?ARWNWPW`@o@RYPWR[NUNUPYPWb@q@b@o@RYNWNUBCNUFKJONURYNUPYPWb@m@b@q@NURYNWRYPWNWd@s@PW`@o@RYNWRYNW\\g@FK`@m@b@q@d@q@LURYr@gA`@o@RYNWPUPYb@m@PYPWNWRWPW`@m@d@s@b@q@NUd@q@PUPYf@q@b@m@b@k@RWPURWRUPWd@k@f@i@h@o@RUd@g@@AnAsAh@i@zB}B|@{@|A}APSRSh@i@h@i@|@}@z@{@f@i@h@g@TWPQFIJINQDCRWTUf@i@PQfAiAr@s@bBeB|@{@|@y@z@{@TSTUPSRSTURSRSTUPQRSVWPQVYl@m@TStCyCDCd@g@RSTSDEPQRUPQZ[NONORSVWNQh@g@TWJKX[@ATUb@c@TS~@_APQTSh@k@RSPQTUTUz@{@|@}@d@g@h@k@VWPQlAoAb@e@`A_AXYPQHIXYRSj@k@RURQRSh@i@n@o@RSLMRSx@y@j@m@RSf@g@~@_ATURSPQRUTURQPQ|@_ARSTURQj@m@DEBCHIRSRSRSXYJMDCRSPSh@i@NOJIJKHK^_@TSPSl@k@VWHKZYv@y@VWVWLMTU@At@w@TUFGLMPQRSBARUDCLOLKFIRSf@g@@ANQVUNO@ATURSJMZYTWDELMRSPQVWTULM@A`AaAPQTUlAoAJIBEFERS?ARSRSTUPQh@i@TUf@g@h@i@PQHKXW@CBA@CRSPQh@i@f@g@TWRQTURSTURSHIn@q@VWRQTUh@i@JKf@c@l@k@\\YTSRQVSPOVSRQhA}@j@c@b@[VSTOVQROVQn@a@TQROPKZSTOVOTOTMTOTOVQTMVOTOVQTOTMXQTORMXQTOVOTQTMTOTOXQTOTMXQROTMTOFEPKTOVOVOVQLIDCTOXQTOVOTORMVQTMl@a@|A_ANMFCTOTOj@]XQl@_@TOVQj@]VOVQj@]ZURMn@a@n@_@l@_@j@_@LIHGRM@?VQRMTOXQRMXQl@_@TOJGZSp@c@VOn@c@NKj@_@\\Ul@_@f@]ZSVOTQxA_Al@a@l@a@l@a@TQVQTOTQTOVQTObAs@nA{@`@Y`@W\\U@AVOTQTOVQVQb@Yb@YPMl@a@l@a@d@[^WTOVQTOdAs@j@a@d@[ZSn@c@n@c@h@_@bAo@rDeCTONM\\SVQTOVOHG`@UfAm@TMVOFEd@WXQTMbDuBl@]JEJGVKhAi@TKp@YTI|B{@r@WPIXK`Bo@fAc@XMbBo@fAa@p@YPG^QVKXKp@YTKJEd@QXKTKXKTKr@Yp@W^Of@SfAc@t@[RIp@W^ONGjAe@TKhAc@hAe@BAVIfAc@l@WXKVMVKXKn@WXMn@UXMTIXMXKTKp@YTIp@YXK@?VKTKZKVK@ATIJGLEVKVKXKRKXMPGFCXKVKdAc@`@O`@Qr@Yl@WlAe@fAc@TIZM~@_@LGVKRIZMTIZMTKXMTIZMVKVKTIZMVKp@YZMh@S\\Oj@UjAe@b@QHEXKp@YXKTI^QPGVKVKhAe@ZK^QLEZMTKXKVKVMl@WZMZMRIVKTKXMVKVMVKXOn@Y`@S`@SDATMTMn@[l@[ZQRKBCTKDCh@YTOVMFEf@Yj@]p@a@h@]XQn@_@VOPMNKh@[b@YfAq@`@W\\Sp@a@j@]PMZSn@_@VQl@_@JGJGPMHEd@YZQj@_@DCf@]jAs@|@k@JEJGTO@ARMZSPKBCRMHEd@YRMVQVOTODCPKPKBCTMBARMTQ\\STM?AVOTOTO@?RMVQDCNKXQTMNKFEVORMDCTODALKJGHETOXQPKBCTOTM@AVOTOXQRMXQTOTMRMDCt@e@b@YTOXQJGHEn@a@TOTOVOVQJEJIRKVQTMVOJIHGXO@ARMTM@AXSNI`Am@DCPM\\Sj@]PMDATO@AVOROHELIVOXQPMXQn@_@RMVQHE@ARMRMv@e@j@_@HETMTOXQBCLIRMd@YPKRM@ARMRMZSNIDCTOPKFETOLIFEb@W`@WbAo@VOVOXQ?ATMRMVORO@?VOZS@APKTOTM?AXOj@_@VOVOf@]`@WLGr@e@vA{@|@k@pAw@bAo@\\U|@i@bAm@dAq@l@]l@[NKHEl@[ZOLG^SVMHCLGPI^QRKVKt@[p@WtAi@b@M`@Ob@O\\Kp@SVIr@Sp@Qr@Op@Qr@OVGdBa@~Bg@`AUb@KbAUFA`Ci@hAW^K|A]xCq@fCk@`@KFAbB_@lAY|Bi@b@Kl@M|A]ZILCHC|@SnBe@DATEzCs@t@OJCzBi@|@Sx@QdBa@x@QJCzA]^IjBc@t@QfAWfAU^IXGDA@AXGFA\\IfBa@dBa@FA`AUt@Qp@OlAYrAYj@MZIhAWj@MXGFCdCi@d@Md@K`B_@XGx@SfBa@x@Qr@QhAWv@QdAU|Bg@r@QVG`@Ij@On@MRERGbAUNCNEbAUr@Q~@SlAYVGvA[x@SB?f@M|Bg@j@Mh@MNEr@OPEb@KpCo@dAUHCd@KhCm@lAWdBa@fBa@p@On@OdB_@RGjCk@PEbBa@d@KLCn@OlAY@?`@I`@KNEPEVGJA`@KDA`B_@HCXGTEfBa@LC`@KhBa@bAWpDy@`AS@A`@I@?p@QdAUTGNCNEJCXG\\IJCt@On@Ov@Qv@Qn@QbAUd@KjAWd@K^KVEBA~@ULCfAWTEjAWXIp@OjAWt@QLCx@SfAW^If@K~@UVGZGDADA\\IPE~@S\\IvCq@|@QTGp@Qn@MvBg@LCr@Ox@S|A_@~A]jBc@bB_@`AUzBg@~Cs@~@ShAWbB_@JCvA]PEbAUnAYvA[FCv@Oj@ODAt@QREr@OREp@Q`@IHCz@SdAU@?FCd@Kj@MhAW`@KDAn@Ob@IRGLCb@K`@INEt@QXGFAx@SFAf@Mb@I`@KbAUXGJCd@KbB_@@?r@Op@O\\GBAb@Ib@Ib@KHAb@IPED?n@MTEVEVEb@I`@I`@Ib@G`AQd@IVETC@Ax@MTETEt@MVETE`@GfAQn@KrAURE^GlAQf@IXGpB[@A`@Gj@Kl@KNCNCPC^IB?lB[jDk@`AQB?`@IfBYHAj@K`@IXEVEFAtASt@Mh@ITE`Cc@FAD?TE|@O`@GVEp@KREj@KfCc@r@MZEt@M|@OfAOnB]b@G?Ah@K^GFA\\EREXEVENCJAXEVGXEXGXEXEXEVEZEXGlASr@MlASXGXEZGD?b@IFAXEXElASVEr@Mn@Mv@KXGLAd@IZGVEXGXEXGXEXGXEXEXEXGXEXGRCDAXEVEZGXEXETEBAl@KD?XGXEXE^IRCXEXGXEXEr@MXEXGTE\\GLAJCVEXEXGZEXEVEZGVEXEXEJCLCXEXEVGZEXGVEXENEHAXEZGVEXEXEXEXGt@MpAUpAUNA\\Gp@Mh@IJCt@KRCr@Mv@K|@MHAXGZGD?j@MVE^IXEDA`AMx@OXElASTEbBYJCj@KVEt@Mn@KTEx@Mr@MJANCl@K|@Oh@IZGdBY\\GXEHCx@MJAn@Kr@MhAQPEzAUVEr@MXEZGPCBA\\Ev@Mj@KDAFAdAQTED?hASf@I~AY@?pB]D?tF_ANEn@KjAShBY\\GhAQfBY@AVEb@GPCVGJAd@I\\GZEjASn@M@?ZETEBAVEr@Mr@KXGPCDANCFAZGr@KZGVEp@KXEZGZGTCBAr@MPCFAXEXGNCXEB?^GjASDAVETCJCh@Kp@Kh@KFAPClASlAQZGr@KRCBAn@Kv@Ot@MZEp@Ml@Kr@MZEt@Mn@KBAXEv@Mn@KLC`@GZGNCb@Gr@Mp@KJCPC|@OJCZGd@GPEHAd@IZEDAdAQp@KZGZEVEd@ILCr@KRCXG\\G`AOd@Il@Kl@Kb@IRCZGVEvAUj@Kt@MRCVGXEHALC\\EVGD?PEZEVEXGXEXEXGXEp@MZEVEXGXETEZGVEXEr@MXEZGXEb@GxAWb@Id@ILALCXGTEB?`@INCXEXEXEXGVETE^GVEVEZGPC\\GXEXEZGZETEXGXETEXEZGNCFAZEVGb@Gb@Iv@MZGVEVEZEVEVEZGVEZGXEp@KXGXEVEZGXEXEFANCXEZGXEVEXGVEB?TEXEXEXGVEXGXEXGXEVEXGZGXEn@Ir@KVG\\EXGTCZGVE\\GZETEZGr@MHALCZGTEXEn@Kr@KXEVEr@MXGj@KDAXEZGTCr@Md@GNCVEVEZGVEXEXGXEXEXGlB[NCZEVEXGVEZEXEVEXGVEZEVGXEZE\\GREXEp@Mr@Kp@MJAf@IXGVEZEVGZEVEZGVEVE\\GTEXEXGXEVE\\GTEXEVE\\GTEXEXEXGRC\\GXEZGVEXEXGXEVEZGVEXEVEVEZGXEXERENCNCVEZGVE`@GPEXEXEpB]JCZGXEXEVEXEVEXGXEXEXGXEXEp@M\\GTEVEXEVEXEZETEXEh@ILCTEXEXEXGVEZEVGXEVEXE`@IRETCl@KHCvDm@`@I|@Mz@OfAQl@K|@OrAUd@G^GLCt@MnDk@lAUr@K|@O`@GFAjB[~@OhDk@fAQxCg@d@IfF{@fAQn@KbAQr@Mh@Mb@ILCp@OhCu@r@SXIr@UZIfBk@jAc@tAi@r@[b@SVKFEh@Up@]RKp@_@RKzAy@bBaAjBgAXOXQj@[JGFEBATMn@_@n@_@PKZOVOBANIVQTMj@[p@_@n@_@PKXOj@]XQj@[XO?Aj@[rBkAXQZO~BsAv@e@vAy@fAm@nBiAzAy@\\UzA{@dAk@LIp@_@n@_@NIFETOVMn@_@n@]TOl@]VORKfAo@VOl@[j@[n@_@l@_@PI\\S`@Wb@UHEJGl@]TOJERMPI\\ULGb@WJEPMZQBAf@YVONIFEVOVMTOPIBCVOTMfAm@TOXORMVOVOrBiA@Az@e@\\UXOTMTMVOTMXQTMdAm@TMj@[RMBAVObAk@l@]ZQPMXOVOf@YBAvDyBTMNIFCXQRKn@_@VOj@[n@_@h@[BAZQTOl@[TM|@i@p@_@\\Sh@[TMVObAk@n@_@XOj@[v@e@d@WVOh@YZQj@]ZQj@]n@]v@e@DCDCTMTMXOn@_@RMVMTOVOTMVMRMXQTMn@_@l@[RMZQRM@?TOXOLGFERKBCTMTOXOTMBAj@]RMXOVORMXORMVMXQTMj@[XQ|A{@\\SrBmAfAk@`Ak@bCuAfAm@h@[~A_ArAu@fBcATM|A}@rBkAr@a@lBgAn@]dEaC`CuATM|CgBNINIz@e@|A}@lAq@rAw@nC}AlBgAbAm@p@]fBeAd@W^STMnAs@XQZStAu@l@]x@e@x@e@VOVORMNIJGTM^SLIPIBCXOPMXOZQLIr@_@l@_@TMr@_@NK^SZSb@UXQPIl@_@BAn@]PMVMXQVMJGt@a@VQn@_@j@[TMZQh@YZQ~@k@VO^SLIXOj@[l@]VOl@]XQTMLIFCNIZQZQbAm@XOl@]j@[l@]VOVOl@]VOn@]RMVORMVODARMRMFCPKj@]JEz@e@HELIj@]b@W`@UVOp@_@v@c@TOjBeADCb@Ul@]NKFEl@]HEPKZQvAw@DCLIj@]XOn@]TOTMVMXQXOf@Yh@[ZQRMXQTKJIPK`Ai@XQRMn@_@@?RMVMRKTMn@_@n@_@TMp@a@t@a@JEj@]XQVMl@]TMPKLIb@WTO`B}@TMd@WxBqADCRKTMLGDEXODCf@Yp@a@n@]bAk@PKl@_@@?bAk@^UPIf@[\\SJGb@W`Ai@rAu@nAs@RMVOXQLGd@Yh@Y^SZSJEPMTMVOZQLG\\SVOh@[\\SRKXOl@]TMj@]NIZQn@_@TONG`@Wf@YBAl@]XQTKXQh@YVO`BcAbBaAx@g@FELIb@WlAy@HEx@k@NKVQXSxAcAj@a@TQTQTQTOTQTQRQl@c@TQTQTQBAPMTSj@c@f@_@lByA~@s@\\Y`@YPM`@]j@a@|@s@VQjDkCVSr@k@`As@FGf@_@b@]`@YBCdAy@vAeAl@e@hCqBfHoFDERObAw@b@]XSTQr@i@VSJIROlCqBJIbCkBh@a@vAeAdAy@lBwAhBwAj@c@j@c@TQTQVQROTQPOVSl@e@j@a@j@e@NKBCVQ@AjB{ARObAy@`Aw@`Ay@z@s@v@q@HIp@k@JKNMVUBETQjBgBj@g@t@s@RSh@i@t@s@@AfBcBpAoAl@k@d@c@f@g@TSrAqA`A_Ah@g@NQRQTUTSTUPQ|@}@RQtDoDbAaANOl@k@h@g@RSd@e@~@{@h@i@f@e@HIHITURQVUPSRQ|@}@TSTUTSLMBCPQVURSRSTUTSf@e@Z]LKRSPQNMlAmARU^]\\]r@q@RSx@u@BCh@i@~@{@h@i@h@g@RSJMHERUTSrAsAb@a@TSRU\\[bB_BTSTUTUTSh@i@RSrAoAVUPQTSd@c@t@u@ROXY|@{@TUd@c@b@a@Z[d@e@b@a@RUl@i@h@g@^_@Z[\\]XW`@_@TUJIBEzAwATSRSf@g@f@e@X[TQZ[b@c@~@}@~@}@|@{@d@e@\\[v@u@HGd@g@VUfAcA\\]DEPOTUTUTSTU^_@NMNOZYHIb@c@TUTUBCRSXU\\]VWz@y@RQzByB|AyAx@w@^_@\\]RSDETSRUVSJMDCh@i@fAeAVUDEFGb@a@~@_ADEBC^]VWf@g@b@a@FGRS|@}@hAeAt@s@ZY`@_@~@_AfBcBd@c@LMXWpAoAjAiAbA_AjAiA?AJId@c@XWDGJKLMJKHGNMJKv@w@\\]r@s@h@g@ZY^_@|@}@RQNSdAaAl@k@~A{AbB_BlAkAnAmAvDqDDEPQVWx@u@FGz@y@f@g@TUf@e@|@{@f@g@JIDETUTU|@y@h@g@\\[^_@NOj@k@TSh@i@z@w@~@}@FGBCVW\\YHKJIzAyATUTSZ[~@}@RQPS~@{@HILMXW\\]POFI@AJKZ[FEp@q@RQTUTURQTUf@g@HGJKVWn@k@x@y@pBmBVWTSPQTUTURQTUTSRSTUpAoARSRSVUh@g@PQRSTSTUj@i@RQRSRSRSVURSRSRSh@e@TURQRUh@g@TSRSh@i@LMFGRQRSTSRSVURSPQBAJMJIf@e@TSjAkALMdAaAh@i@~@}@RSh@i@|@{@~@{@~@}@hBgB\\[^_@x@w@NMv@u@^_@`@_@lAmAz@y@v@u@h@g@bAaA~@_AlAiAh@g@nAkARSl@o@z@w@rAoAZ[xPePZ[~XeXt@s@JIPQTSRSTUJId@c@`@c@POBCRSRQRSRSj@i@h@g@BENMRSTSRSTSRSTUf@e@tAsARQVWpJgJTURQRUTSBCPO^]RUHG~@{@TUTURQTSRSRQRURSBAPQRSRSTSpEkEvFoFTSRQRUTSTSRSTUzFsFJK\\[VWPOpAqAf@e@TSf@e@PSTUTSRSPQj@k@TSRSTSRQTSVURQj@i@RQTSRQ@ARSVWRQPQBCTSRUPQVSRUNORSj@g@h@k@|@y@h@e@RSVWPOTSh@g@TUTSRQTQRQTSRSTSVUTSROTSRQTQTSTSTQRSTQTSNMDEVSTQFGJIROTSRQVURQvAkAh@c@TSf@c@XStAkALKp@k@XUh@e@ROf@e@l@e@TUPOTQ`Aw@j@g@vAmAh@c@RQh@g@TQn@g@h@c@h@e@POPODCRSTQj@g@z@u@VUTUVSPOVSJIHI~@y@v@o@\\WRQpFoETQRSTOBEjFkE\\YzEaEVQl@i@`@]LKTSvAkA`BwAd@_@xAoAhAaAjAaAVSZYNMj@e@nEuDbA{@fCwBf@c@rAiAtAiA\\YfB{A\\Yl@g@XUNMHGFGXW^YTSPOJI^[d@a@j@e@r@m@JIFEjEqDbO_M`Ay@LKrAiAd@a@NM\\YTSx@s@z@s@^YVUrAiAj@g@@?f@c@RQVWJKHGf@e@RSTSRSRSf@i@PQ|@_ATWf@k@d@k@RSX]\\c@d@k@HKX_@RUf@q@DE`@g@b@k@d@o@`AoAZa@f@o@t@cAx@eAjA{Ad@o@lA}A|B}C~EsGRW\\a@V_@RWx@eAv@cARWh@s@~B}CV]tAgBX_@RYjCiDBEb@k@RWPUTYJOx@eAb@m@RWd@k@LSf@m@T[`@g@T]r@}@BEj@q@V_@d@m@RWRWRWd@m@NSd@k@dCcDFIFIPUz@gAx@eAt@aA|AqBd@m@RYhAyAf@q@b@k@RYhAyAx@cARYRUdAwAh@q@b@k@x@eABELQ`@i@f@q@RWd@m@v@aAb@k@d@o@RWv@cAf@m@R[X]DGRWBC^g@h@q@d@m@LQV[?AX_@FGf@q@b@k@RYRWb@i@fAyABCTYn@}@h@q@FIxBuCv@eAb@k@Za@h@s@rEcG@?p@}@Za@X_@rR_WbAqAt@_AzAoBbCcDZa@x@cAd@m@b@k@lA}AZc@FIPUTYhAyANUJMLOt@aABEp@y@BGb@k@@A^g@r@}@j@u@JOn@y@LOPU\\c@xAoBJKPUPW|AqBj@u@v@cAhAyABCJO^e@DGPSJMX_@nA}ALQpA}Ad@m@DE^e@PQTYf@k@JOX[HK\\_@d@k@RUz@_Ap@w@DELMj@o@\\_@VWJMb@c@j@m@TU^a@|@}@DGv@u@xA{Ax@y@^_@Z[JKDGb@c@FGPQTU@Af@g@^_@HKPOVWRUJIZ]TS`@c@FGNODETU^_@\\_@f@g@TURSRUdBeB\\_@LMr@u@l@m@VYNOh@k@h@i@LMDEHKJKl@o@b@c@@?Z[^a@h@i@b@g@VUf@i@|@_Ah@i@v@y@VYx@{@Z[v@{@z@_ATUd@i@RSTWTUd@i@f@k@^a@X]BAvBeCPSRURSPSRWPQX]RSFIX]@?X[|AiBz@aA|@cAv@}@pAyAv@_An@s@X]FG`BmB@Ab@k@RUTWRSj@o@LOBCZ]FI`AcAd@e@h@i@h@g@h@i@LMn@m@h@e@RSTSj@g@LKXWBCRQLKFERQZWh@c@RQpBaBpBcBlDyChI_Hb@]|AsAhA}@tAiAbBwAx@q@\\YzBkBv@m@VUb@_@ZWTSh@c@TSDCbA{@lAcAVUl@e@h@e@b@]tAkA^[jDsCDCZYFETSRQHGzBkBzAoARQPOz@s@bA{@f@c@bCqB`Aw@@CvD_D`@]TQRS`Aw@`@]DCd@a@bA{@lB}Aj@g@RMTSbAw@dAw@vAcATQj@a@PMZUn@a@zAcAl@_@h@]p@a@DEf@YTObAm@n@_@`Am@tBqANKr@c@XOn@a@rG}DhFaDTMTOLI\\SvBqAdAq@dAm@`DqBhC}AdAo@|BuAhBgAbAo@RM\\STOVQj@]bAm@JIz@g@VOVOTOVOXQTOnBkA`@WLIn@a@^U\\Ut@e@f@[DCVOj@]rBoA^U~BwA\\SNKDA|CmBfAq@^UtAy@vA}@d@YLGpBmAl@_@h@[dAo@TO@?PKRMPKr@c@j@[NKl@]PMr@c@h@[DCXQRMHG^U|A_AVQn@_@l@_@n@_@v@e@JIdAm@zA_AdC{A~ByAb@W|A_Al@_@|AaAVOj@]|A_Al@_@l@_@BC`Ak@l@_@n@_@l@_@l@_@VQTMVOdAo@TOl@_@VOl@_@l@_@VOTMVOTOVOXQTOl@_@n@_@h@]ZSTO~@k@xA}@TOVOp@a@NIVOVQl@_@VOl@_@VOj@]l@_@bAm@ZQbAm@JGNKRMj@]|AaAdAo@XQPKXQDELGFEPKbAm@|AaAl@_@XQXOhBiAl@_@BAFELIRMn@a@TMLILIl@_@TOl@_@h@]p@c@HELIl@_@XQTOVOTOTMTOVQVOj@]p@a@TORMn@a@^Uf@YDEf@YVOPMfAo@~AaATOJIDCXOXQVOROTMVOHGJGRMBAXQXQPKVOTOTOVOVOTOXQRKj@_@VOp@a@x@g@hBgAVOPMrBoAt@e@lBiAfAq@LGDEVOTOn@_@l@_@VOVMTOVOjC_Bl@]VOTOVQTMVOVOTOn@a@RMVOLIFCVO@ATOVOVOTOVOTOVORMXQVORMXQVOTOTOVORMXQVORMVOTOVOTOXQTOVOTOTMn@a@TOTMl@_@TOtBoAp@a@l@_@l@_@zA_AdAm@j@]FE\\UjDuBvA{@tD{BhAs@l@]VQLGHGTM?A\\Sb@WVQfAo@l@_@`Am@bAm@BA^WJG^SJIlBkADCXOTO`BaARMl@a@j@]VOVQj@]bAm@XSTMVOTORMXQTOVOTMVOTOdAo@zA_AVOTOl@]n@_@bAo@n@_@TOTOZQh@[j@_@l@]|A_ATOl@_@l@_@|A_AdCyABCTMDCf@[h@]VOZSTMTOXOTORM`Ak@r@c@j@_@dAo@rBoABAh@]b@WHGTMn@_@bAo@VOTMNKXQRMb@Wb@WVOd@[\\S@Ar@c@~@i@r@e@RMZSVMzFoD\\UxHwExA}@zFmDbBcA^Ux@g@n@_@RM^Ub@Yx@e@lAu@\\SlEoC^SfBgAh@[lCaBBCTMRMl@]p@c@dCyAZSVOj@_@n@_@bCyABC|@i@^U^ULIvBqAbEeCTOjC_Bl@]ZUh@[TMn@a@j@]p@a@VOl@_@`@WXQb@U~@k@~CkB|A_AxA{@XQVOTMZSd@[n@_@LIFEVOTOFELGTOZQRMj@]FE~@k@FEFE`@UnAw@bBeAl@_@bAm@bAo@n@_@XQv@e@hAs@~CkBFE`@Wj@]n@_@LI^UTMBCPKVOZSb@Wr@e@tAy@fAs@ZQ|A_AtBqArA{@l@_@zA}@l@_@ZQ@Ax@g@^UNI|A_Ar@c@RM~@k@VOTOLIz@g@RMtBsAz@i@^UTOvA{@l@_@~@k@t@e@hC}AxA}@p@a@~@k@jAs@PKVOVObAk@n@_@l@]TOVOJILGPKp@a@j@]zA}@BCTMVQ`@U^Ul@_@p@a@lAu@ZQp@a@TOPKVQFEtAy@dAo@bAo@VOHE`@W|BuApAw@f@[bCyAvBqA|BuA~AcA~@k@TMVObAo@RMRMZQfAo@\\Uf@YRMfAq@pAy@z@g@TMJGNMVMVQ\\S~@k@v@e@`@W@An@_@x@g@r@c@FEVOPK`Am@h@[|@k@^S^Up@a@j@_@vG_Eh@[XQj@]TOPKp@c@NIz@i@HELI^WTO\\S`@W\\Sp@c@rBoA\\Sh@[f@Y`@WlBiANK`Ak@NKb@WDCNKNGl@_@h@[XQ\\Sn@_@VO`@WbAo@LKVONI`@Ul@_@`Ak@bAo@VOb@WZSJGFEbAk@zCkBzA_AVOZSr@c@hBgApBoAdBeAvA}@rAw@\\U^SFEv@e@^UZS`Am@PKJG^Ux@i@BAb@YtAy@hC}AXOfAq@tAy@r@c@|BuA`@UzA_Ad@YjAs@dAm@?Al@_@~@k@l@_@hAq@TOHETONIl@_@pBmAbC{A`Ak@fAq@t@c@|@k@d@YFEbB_Ar@e@NITONIRMVOFELIVOTOLGFGTMXQTOTOXOTOTOVOTOVOVQTOPKBAVQTOTOVQTOVONMDCVOROTOVQTOTQVQROTQVQTQTQTOVQTQVQTOTQTOTOnBqAdAs@VQTOTOVQLIFETO@ATOROVSl@a@TOj@a@TQVOTQTOVQTQTQl@c@RMXSRMTQLIHGTQTOTOVQTQl@a@ROZUPMPKBCTQTOTQVOVSROTOTQVQTOVSTO?ATMTQTQTOTQVQTOROVSTOVQTQFEJIVQVQTOTQVOTQTOTQTOTQVQTOTQVQRQl@a@TOVQTQVQTQJGFGHGtF}DdCeBVQzEiD@ArFyDzAgAxB{A`GeEdEwCXQTQTQTOTQVOTQTQRM@AVQBCPKTQTQPKXSNMBATOTQVQTOVQVQVQf@_@l@c@n@c@ROROTO@AXSh@_@l@a@\\WLIROXSROl@a@j@a@XQTQTOVQj@a@j@a@ROTOTQl@a@XUPKJIJGTQj@a@p@e@tAaAn@e@LI`Aq@VSVQJIl@c@LIZUNMNKTOZUTO~@q@nBsApDiCbIwFzB_BNKr@g@FEr@g@v@i@|@o@HGl@a@TQHG`@YzB_Bv@k@VQTObCeBbAs@LKHGTO^Yx@k@j@a@ROVQTQVQbAs@lBqAVS`Aq@l@a@bAs@j@a@hEyCrDiCzCwBVQf@_@hGiEbIwF\\WVQ^Ub@[nFwD\\WRMHIlBqAr@g@n@e@dAs@JIROp@c@RQVQTOVQRM^Yj@a@d@]z@m@d@]p@g@x@k@^Yf@_@JGb@[l@c@x@m@PMb@[p@c@v@k@dAw@n@e@`Aq@TOLKPMRMFE\\UHGRO@APKJINMJGVQVQXSNKn@e@TODEb@YXUTOb@YPMb@[ZSXSDCZU\\W^Y`@WZUd@]DCp@e@lA{@rA_A\\W\\WTOBCZS\\W^Wd@[|AiAp@e@v@i@j@a@j@a@HELIVSj@_@nBuAbAs@RO^WVQd@]fBoArF{DNKrEaDPOJGxF}DvAcAdCeB~LwI~AiAXQl@c@tCsB|BaB`EsCt@i@f@]`@Yf@]l@c@^WPMj@a@b@Yl@e@^Wj@a@VQROZUXSRMVQl@c@b@Yj@a@LIr@i@\\Un@c@BCTOFELKNINMVQRMTQHGn@c@x@k@FGXQb@]XS^WdAu@l@a@lBsATQl@a@l@c@h@_@l@a@VSTOj@a@|@o@JGDEHGROh@_@xAcA`As@dAs@~@q@`Aq@|@m@^YLI\\WlBsAJI^W?ARMVQh@_@l@c@bAs@l@a@p@e@|@o@HG^Wp@e@ZUJI~@q@XUXU\\WBC\\[XSDEFGTQ@ARSTQZ[VUf@e@JM@?RUTSLOXYPQRURUj@o@FGJMPSd@m@JK?AX]LOV[LOT[NURWNSt@iAX_@NUHIPY@APWPUxAwBfA_BRWVa@DEZe@dBiCRYNSRYnC_ElAeBhAcBHKNSfA_BPYb@m@NUBC`@m@NUJOV_@fA_B`@m@NSzAyB^g@`@o@Zc@`@m@r@cAPWRYFKFI`@m@d@q@b@m@DIvB}CV_@fBgC|A}BbCqDPWl@{@FINUDIj@w@lAiBnAgBf@s@dA{Ab@m@r@gAp@_AhAaBLSV_@@CDEZe@R[JMHMn@_AHKFIHKv@kAb@m@d@s@RYb@o@fA_Bz@oAz@oAFIXc@\\g@V_@t@gARWh@y@NST]RYLQLUX_@HKLSLQ\\g@NSf@u@|@qAvAuBVa@DGHIDILOhDaFrAmBBEHKpAgBbBgCrCeEtBwCt@gAn@aAl@{@tCeEn@cArAiBbDyEVa@nF}HbCmDzA{B~BiDZc@jBkCT]`BaCLSRWPYv@gAT_@PSPYfAaBHMDGNUPYLQb@m@zCoEZe@l@y@FIPYBCZe@RWZc@NUDIV]^k@Va@PU`AwA`AwA@AFKb@m@rCeEDEx@kAT]d@q@|@sA`@m@|DwFbCqDp@cAZa@^k@d@o@LQVa@l@{@Xa@Ze@b@m@PWDIHKbBcCT]Ze@JM^i@JObAyArAoBFIX_@Va@JODE?Ab@m@lBmC`DuEjF{HLQvAsBfAaBbEaGrAoB@APWf@u@r@cAjCwDrB{Cr@cAhBkCjOwTd@o@PYp@_AVa@\\e@DI`AuAr@eANQd@s@jBmCd@s@DE^k@^i@b@o@`@k@v@iAt@gA\\g@Xa@NSd@q@p@eAbAwAh@w@T]h@w@Xa@l@{@Zc@T]T]Zc@PWNSPYPUPWRYPWLSRYNUHKHKV_@^k@LOHM^i@|@qA^i@`@m@n@}@PW?AT[`AuAf@u@PUVa@LQ`@k@`@m@Xc@X_@T_@NSNUFIb@o@HMd@s@FI`@i@v@kAFKLQHMXa@LOZe@lAgBHMT[@Cn@}@HKFKPWb@o@hA_B\\g@V_@NU@Ab@m@j@{@V_@f@s@p@cANQj@{@X_@j@{@DIRYFGPW?ANSFI@Af@u@l@{@JQT[LQR[NSNUl@{@NSDIDGd@q@`@k@|@qAHMJM`@m@JOLQb@o@PWb@o@b@m@h@y@JMHMHMX_@T]hAaBRYJOT]NUT[NURWR[BE\\e@f@u@x@kAnBsCj@y@p@cAp@aAr@aADIJOHM@AJO\\g@V_@BCNUb@m@PYRWJQRYNUHKHMb@o@d@o@PWr@eAl@}@d@q@\\e@~@uAt@eAFKV_@h@u@FIrAoB`@k@PYV]Ze@JMLSJOJODEFKZe@V_@HKPYRWXa@DG\\g@|BeD?A\\c@Va@Xa@DGd@q@JOb@m@HMDIPUJOT]b@o@b@o@`@k@R[V]JOb@o@PUd@q@Va@RYh@w@@AV_@n@_Ah@w@FGj@{@LQDIHIdA}ARYXc@JMDGXc@FIb@m@\\i@DELSPUZe@T]RYPWBCLSZe@\\e@LSRW^k@FIdBeCBErDkF\\i@@?T[LUb@o@x@iANUPU\\g@p@aAd@q@V_@BEb@m@JQj@w@\\g@NWj@y@d@q@NUNSNSDI|A{BJOdBeCVa@hBiCj@{@`AwAhFsHj@w@T]Zc@FK`@k@^m@b@k@BEb@o@PYNSRYNURYb@m@`@o@RYJMR[h@u@^k@d@o@FK\\e@PUNUd@m@NSBEn@{@X]\\c@j@q@RUDGJMp@y@Z]f@i@RUf@g@Z]NOZ[NOjAmAbCcCb@e@f@g@NONObBaBJMRUPOBCFGRSFGl@m@RSPQ|@_A@A`AaAv@w@d@e@BEf@g@RSh@i@BC`@a@l@m@f@i@PQBCTUZ[\\]RS\\]FIj@k@f@g@r@u@r@s@BCb@c@f@g@^_@@A\\_@@APO?AFG\\[PStAuARU|@}@RSh@i@h@k@z@{@TUzB}BhAiA|@}@VWb@c@TURU\\[\\_@TURSh@i@PQRSVWf@g@h@i@f@g@fBgBZ]JKp@q@TSr@u@tAwA~@_At@u@HIJKPQTURSRSTUx@{@f@g@h@g@j@m@d@c@?Af@g@h@g@TWRSRSPSHI`@_@RUl@m@lBmBDG~@aATS`@c@TSRURQb@e@VWTUh@i@|@}@VYLM`@a@h@i@b@c@~@_ARU`@a@@Al@o@f@g@TSh@i@\\]BC\\[RQ@ARSh@g@TS?ARQlAgAHITSRQTSRQTSTSTSTQTSTSTQRSTSTQTSPOBATSTSTQTSTQBCPOTQTSTSRQVSRQTSTQTQTSj@e@TQTQTSTQNMDETQTSVSROTSTQTSTQVUTQ@APOBCPOVSTQTQRSTQVSTQTSTQXUNOVSROTSTSTQTSNMDCTSVSRQTSTQTQTSJIDENMROVUZWb@_@TQRSVQh@e@j@e@l@g@TSVUPOTQTSTSTQTSRQl@e@TQTSTQTSRQRQFGNMTQRSRQVUVSRSRQVURQTSRSTQLKZWRSBAPOHIHIPMBEDCRSvBiBhAaAvAoAn@k@PQRSRQBCNMRSh@g@RURSTURQVWTSRSRSTSPQTQVWPOTURSTSTSNMTUHIFGFGRSTSPQ@AFGJKVUDELMRSh@e@HILK@CRQTUTSRSTSTSRURQVURSRSTSRQVUNOBCTURQTSTURSTSRSRSVURSRSTQHKHGTURSTS@ARQRSRSTSVURSRSTSRSTSRUTSLMFELMFEBERSTSTSRSPORSTSRSTSRSTSRUTQTURSRSh@e@TUTSRSTSRSTURQTUTSRSTSTSRSJIHITSfAeAJITSTSRUTSRSVURSPQBATURSRSTSRUd@c@j@k@TSRQTURQJKFGTS\\[NORQ`@_@JKl@k@z@w@b@c@t@q@TUjBgBjCeCbFwEjFaFvCoCzAwA`D{CnCiCp@o@v@u@j@i@|@{@FEzHoH`DwCrCiCjAgAtDaD`FkEz@u@tAkArCcCPOHGLMRQTQTSTSTSRQVUPOTSVSRSTSTSTSh@e@TQTSRQTSTSVSPQVSTSBCNMJKHGVUPOVUTSPOVSRSVSTUPMTUTQj@e@~@{@l@g@POTSTSTSRQj@g@TSTQ@ARQDENMTSRQTSTSTSTQRSHGJKTQl@i@RQRQTSTQRSl@g@RQBCNMl@g@h@e@VUFEJKRQTSTQTSTSVSPQVSRQRSNKFGRQh@e@TSTSTSTQTSRQTQTURQ^[NMPOHIJITSVSRQTSRSVSRQTSTSPOBCTSTQTUPMl@i@l@i@HGv@s@t@m@\\[VUVSNMBCTSPONMBCh@e@lBaBfB}ADCb@a@XUTSTSRSVSRQ@ARORQTUVSj@e@RQVUJIFGJI\\[j@e@TSTSRQTSHG`@]~@y@~@y@FGNKTSRSTSTQjBaBTSTQhBaBTSTSh@c@`Ay@`@_@HGBCb@a@j@g@TQTSTSj@e@RQVUPOVSNODCRSTSTQh@e@RQTSTSTQTSTQTStAiATSVSRQRS@ATQFGLKRQTSRQVURQTSTSTSRQVURQRQ@ATSTQNONMRSVSDEJITSTSRSVSRQFGLKRQXWPOTSRQTSTSVSRQTSRSTQTSRSTQRQLKHIVSRQTSRQTQVUTSHGv@q@|@w@VSRQj@g@VSPOVURQXUh@e@RQTSh@c@j@g@fA_ANMRQj@e@TSTSRQTSj@g@f@e@~@y@VU~BqBp@k@NMf@e@~@y@`Ay@h@e@NMZY~BsBzF_F|IyHFEFGLKVUDEJIRQj@g@HGJK`Ay@h@e@h@c@VUTSj@e@h@e@j@g@RQj@g@TQ~@y@TSRQTSTQRSVSRSTQTSTSTQRSDCNMRSTQTSTS~@w@j@g@RQHGLKNMNOLMJGLMb@_@JIRSTQTSRQd@a@ZWRSTQTSRSTSTQj@g@~@w@TSDENMTSRQTQTSTSt@q@^[TQh@e@TSTSTSTQTSRQFGDCHIPO@?DENOLIFGTSTSRQFELMTQTSTSj@e@RSTSTQRSVUROTSTSRQVSPQVSTSTSRQRQVSTSh@c@VQRQNODCTS@ARQRQPODCj@g@TQTUTSRQVSh@g@VSRSTSTSRQVUTSTSRQTSRQVWPOVSPQTSTQRSj@c@RSh@c@VSf@c@VUVSTQRQVSRSRQj@g@zAsAROXYLKTSTSTQTSRQTSTSTSRQTSTQTSTSRQVSRQTUTQTSTQRQ?ATQVURQTQRSVSTQRQTSTSNMDERQBAPQPOBANO@?DERQRQj@g@TSj@e@TSTQRSVURORSTSLKFGTQJKHGJK\\YDENMTQRQFGNMRQTSTSTSRQTS@ARQTSRQTSTSTSTQRQTSTSTSTSRQTSTSTSTQTSRSTQTSTSTSTSRQTSTQTSTSTSTSTQTSTSRSTQVSRQTSRSTQTSLKHGPQ@?TSDGNKh@e@TSRQTSTQRSJIHITQRSTQTSRS`Ay@PO@ATQPQn@i@RSTQHIHITQJIHIRQVSRSJIHITQTSTSTSh@e@rBgBnAgATSJI\\[TQlD{C`Ay@TQvAmAVUtAkAj@g@|@w@rAiArFyETQf@c@ZYfA}@^[VS|@w@p@m@FCFGf@c@@ATSVUdA}@lAeARSVSh@e@vAmApAiAZYfA_AZ[l@g@~FcFp@m@`@[tBiBfDwC^[LKj@g@\\YLKLMHGHIVUFETSHIJGTS`Ay@p@m@LKj@g@j@g@JIh@e@`Ay@TSRQj@g@tAkAj@g@p@k@ZY\\YTSj@e@~@y@bA{@|BqBRQTQTSTSZWNO~@w@`Ay@TSb@_@DETS@?~@y@h@e@TSj@g@h@e@j@e@tAmA`CsBj@e@b@_@\\YjBaBh@e@TQTSRSj@e@`@]\\Y~@y@VSTS~@y@TSRQ`CsB`CsBhB_B@A`Ay@h@e@TSj@e@vCeCb@a@FEj@g@HGRQHITSFENMJIFGd@a@ZWtAmAd@a@XUTUVSTSHI~AsAjB_BTSTSjB_Bh@g@v@q@FEVU~@w@j@g@TQRSTSTQTSRQTSTQTSTSRQTSTSh@c@@AJKTQTSTSTQRSVQPQDEPMRQh@c@DEPOJIZYTQTSRQTQBARSRMTQTQTQTQRQXSPOhCsBhByAlB}Ar@i@LKbCoBj@c@lB{AtAgAxCaCj@c@JIHGRO@Aj@e@TQTQTSTQl@e@tC}BJIjA_Aj@c@TQTQ@AvC}BTQTQ~@w@HEhDmCnCyBfEgD\\WjCsBHGz@q@\\Y`@[t@m@`@[xAiAXUf@a@ROXUBA\\YHIRMLKbDiCZWTQPOdA{@lDwCVSPQVUvAmAjB_BtCiCTSRQTUTSRQVSPSDCTS|BqBTUvDeDxBoBdDyCn@i@l@i@j@g@tEcElBaB@Cf@c@DEh@e@POj@g@RS^]JINOFGHIHGj@g@VWZYd@_@d@_@`@]lAcANMLM`A}@@Al@i@`@]l@g@b@_@VSTQ`@[PMFEf@_@JIVQTQFENK~@m@FERMn@a@HEz@g@b@U^UbB_AzAy@jAo@vBiAdBaAdCsAvAu@`B}@`@UlBeAVMl@]PKTKp@_@\\SVMHGp@]n@]@Ad@W^Sf@YFEh@YdE{BzAy@^SRKJGRMr@_@^SBCl@[LGTMLGVOBA^SHGTK~@i@JETOn@]XM`@WLGBAZQXONILILGZQ\\QBCXO`Ag@^SFCf@YVOVOFCh@[TMp@]LIx@c@\\Sf@WnBgAJGPIZQnAs@f@W~A}@TMp@_@TMb@Ub@Un@_@VMfAm@~A}@`@SLI~A{@\\SZQv@a@vF}CVO~A{@|@e@^S~@i@^S`B{@n@]dDiB~A{@vIwETMTM~A{@fAm@VO~A{@fAk@fDiBn@]VOl@]hAm@^SxAw@n@]VMn@_@NGvC_B~A}@b@U`@UhAm@l@]n@]n@]hAm@fDiBl@]r@_@VOXOj@[VOx@a@x@e@XOZQVMVORMZOVO~DyBlAq@pC}AxAw@@AbAk@nBeAJG|@e@h@[p@]f@YrAs@PKp@]z@e@nCyAf@WPKj@Yf@YZO~@g@`@S\\S~@g@n@]vAw@HEhAm@j@[FC~@i@TMBAfAm@lAq@ZQ|BoAFCFElBaAvEiCfDiBNIfE}BvBkA~@g@NIh@Y`Ai@`CqAbDeBZQn@_@~A{@PKp@_@z@e@JGn@]l@[VOVMl@]p@]NKFCZQPKDCj@Yb@WJGTMhAo@DC`Ag@r@_@fAm@v@c@PIl@]PIFEt@a@LGZQTMVMn@]p@_@j@[XO`@Ud@WZQRIXQn@]|A{@jAo@`@UPIRKVOTMZQb@UBAZQNIDCNI`@Sh@[\\Q~A{@bB_A~@g@l@[PKd@WVOVMXQRKVOn@]n@]n@]VMVOVMZQzAy@XOx@c@b@W~@g@JGVMVOVMVOTMVMZQJEFEVMTOXOTMXOn@]d@WHEn@]r@_@XORMTM\\QRKVOZQTMZQRKl@[XQTKVOVMBCRKZQ~@g@BAVOVO\\Qh@YXOl@]VOn@]n@]VONIFEVMZQRKVMZSj@YJGb@WXO@ARKJGJEVOZQzAy@n@]VMDCn@]PKDCPKXMTOVMDCPKVMVOLGHEp@_@n@]VMVOVOn@]n@]VOVMfAm@VMVOPKDATMp@_@~A{@n@]VOXOXORKVOhAm@@ATKTOn@]VOp@]VMVOVMVOVMn@_@n@]VMn@]VO\\QTMXONI@A\\QVORKVOZQh@YXOTM\\SRKr@_@TMVOPIZQXOx@e@d@Un@]n@_@n@]tC}AfAo@hAm@p@]j@[n@]r@a@TMjAm@\\SbCqAVO~A{@r@_@RKdAk@vEgC|A{@pBgAbAi@ZQ~A{@LGHGTKVO~DyBVOTM^STMTMNIVOVM^STMVOTMTMVMVMVMTMVMVOn@[rBgAPIJGVOTMVO@?RMXORKVOTMVOTMFCNKLGHGFCHEDCTMDCtAu@rAs@JGn@]DCNIPIXOBCJGJERMJEDCFEBAPKVMRMDABCPKVMVMTOVMVODCBALGTOVMVMn@]TOVMTMVO^STMBAFEn@]x@c@n@]VMPMDATMHELIBALIj@Yj@[b@UXOdAk@VOVMTMPKDC@ATKTOTOXOl@a@RMTOFELIVQTOVQTQVQTQTQVQNM\\Yh@e@NMn@k@TSRQTQRSXW|@w@NMBCXY^[TUPOl@i@XYhAcARSTQRSTQRSTQRSJIHIRQTSh@c@RSDCTUNMRQ|@y@RQRQj@e@RQRSTQh@e@VSRQ@A~@y@ROh@e@h@e@j@e@j@i@BATSFIf@c@jEyDVWrAkAhD{CJIt@q@pCgC|AuAt@q@VSTURQTSRQf@c@j@i@FG\\Yl@i@TUh@e@z@u@tAoARQBCTSPOj@g@b@a@v@s@FEn@k@hBcBJIHIXURQb@a@b@_@LMLK\\[JKh@e@d@a@ZYd@a@RQXYzBoBrAmA`A{@z@u@h@g@j@g@VURQh@e@j@g@j@g@RQ\\[LKLMDCd@c@LKb@_@POBCrAmAj@g@JIZYBCPORQTSj@g@TUTSl@k@`@]TSd@e@RQDC@ALKf@c@~@w@h@g@@?RSTSTSRQDENMf@c@TSTSRSVSPQj@g@RQHGr@o@l@i@d@c@VUf@c@j@i@h@e@j@g@RSh@e@h@e@h@g@f@a@RSVURQVSf@e@RQTSRQVURQPOVUVUPORQVUNOTSTQVUVUz@s@RQVUPQTQVUNOVURSTQTUNMXWPOTSTSTSNOFGRQRQVUPOTSPQFEVU^]JKJIRQRSBCPMPQTSTSTSVUDEXW`@]FGHILKPOBCRQXWRQRSz@u@JILKRQNOBCVUn@k@NMf@c@XWd@a@`@_@HGRSTSTSLKn@k@f@e@BATSRSNK@CXUJKXWPOVUPOl@i@f@c@XWx@u@XUf@c@VUPQVULKDETSLK\\[RQTSRQh@g@j@e@RSTQb@a@f@c@fAaArAmARQx@u@DCp@m@LKh@e@NORQbA}@v@s@FEh@g@NMBCHIFEXWZWJKx@u@@AXWh@e@d@a@RQTSd@c@r@o@b@_@h@e@j@g@XW@ALKDEh@e@FEt@s@d@a@VU@Aj@e@LMDCb@a@h@e@XWTSf@c@@C~@w@?A|@w@PQVUJIhAaAJK\\[b@_@XWVWPMTSTSRSh@e@TSRQTSPOBCRQTSRQJKHG`@_@p@m@TSTSRQTSl@k@b@_@ROTUTSTSTS|@y@NMDCRSNMj@g@XWRQTSRSNMTQRSZWRSTQLO@?RQFGLKNMBCTS@CVSNMRSn@k@TQNOXUh@g@LMDCd@a@l@i@d@a@h@e@h@g@XWTSRQTSRQTSNM@ARQXWPMNOBCXWTQTSRS@?RQTSTQd@a@NOPOJK~@y@JMp@m@h@g@hB_Bd@a@NM\\[NQx@u@BCTSTSRQTSRQRSTQRQPOdFqEbGmFTSTSRQTSRQTSRQTSRQTSTSRQTSRSVSRQTSRQTSRQRSVSRSTQRSRQTSh@e@TSTSFGLKPOVURQRSTSTQRSTSRQTSRQTSRSTQTUTSRQh@e@RSVSRQRSTSRQTSRQVUPQTSTQTSRSTQh@g@TSLMDCTSTSRQRSTQTSRSPOVUTSRQTSRSVSPQTSRQTSRQTUTQRQTUTQRSVSRQTS|@{@pAiATSRSTQRQRQVURQTSRQTUTSRQTSh@e@\\YJKTSTSRQRSTSTSTSRQTURQTSNOBARSRQTSTQRQTSRSTQTUROVUTSTSLKTUVSVUPQTSTSRQRQTSXWPORSTQRSTSTQTSRQRSTQTSPQ@ARQTSRQTURQRQVUPQLKHGRQRSTSRQRQTSTSTSRQRSTQRQTSTSTURQPOVUTSRQTSRQRSTSTSTSRQDEDCHITSRQ@ARQTSPO@ARQRQRS@?TSTSJKFGNMBCTQFGJKTSTSRQRQ@ARQTSRQVURQFGLKRQTSPO?ATSTSTSRQRQTUTQTSFGJITSRQTURQTSRQRQ@ARQTSTSRQTSRQTSTS?AROTSRSTSTQRSVSPQ@APOVURSTURSRQRSRURSTUNQBARURSPUTUNSTUDGRUDG@?`@i@FIPSd@m@RWPWRWFKFGPYPWNQR]PULS\\k@bA_BR]^q@l@eA@EHMx@{AZo@d@}@LWNWLYLWP]NYNWN[NYJSP]NYN]NWTc@LWP[LYHMDKLWHODINYP[LWPa@v@yARc@l@gATc@P]JUr@sAJUl@kAP[P_@DGBINWLWN[~@iBNWLWNYP]LWLWNYLWN[Zm@DILULW@CP[LWLYBCJSNYLYP]@CLSLYDGHOLYNYP]NY?ALULW@ALWNYNYFOf@aAnAcCl@kA\\q@^u@NY^s@\\s@bAmBx@_B\\s@^s@NWLYNYN[~@gBP_@^q@xEiJbDqGDINYNYNYNYLWNYJSBENYLYNYNYP]NYNYNYNYNYFODINYNYNYLYNYNYNWNYN[LWNYNYLYPYLYNYNYNYLYNYNWN[P[LULYNYNWNYP]N[NYNWLYNYNYNYNYNWNYNYLYNYNYNYNYR_@L[NYNYLYNWJWNYBC?AHQP]NWJWP[LWN[LWLUNY?ALWP]JQBELWNWLYNW@AN[BGHMLYNYNYP_@NWN[JSJQFMLWNYNYLYNWNYDKFMNWNYP]LYNWJUP[P]NYLWNYLWP]NWLYNYLWR]LYNWLWNYP]LWP_@JQBEBEDKR_@Tc@j@gAP]LW@ALWNYVg@Vg@LWP]LU?CNULYBCLYNWR_@HQNYLWTc@JS?ALUP]NYLWNYN[@ALYNWLWNYHOFKLWLYP]NUFODGN[NYNWN]NYLUBGHQP]\\o@N[LWNWP]NWLWLWP]LU@ARa@JUNWLYNWP]LYNW?CNYNYLWNYP]LULYP[LWLYP[LYLWNYN]P[LWJU@CJS^w@N]LUL[N[N[LWFODIP]LWLYLYLYN[LWN]LW\\u@L[N]LWN[LYJYP]JWN[N[JWN[LYNYL[N[N[JWN[LYL[JQBILUN_@JUP_@LYN[JSL[P_@LWN]JWNYLYN]LYN[JWN[LYLYDKHOHSBCN_@LWFMFM\\w@LYLWN[L[LWLYN]LWN]JUN]L[NWN_@JUN[HQDKLWL[LUN]JWP_@LYJUN_@LWN]JUP]JWN[LWN]LWN]JUP_@DKFKN]LWLYLYN]Zu@NY\\w@Zq@^y@JWN[LYN]LUN]JWN[LYN[N[LYN[HSP_@LYN[JWN]BCHSHODMLUN]JWN]NYLYLYLYN[N[JWN[N[JWN]NYLYLYN[JWN]LYN]NYJUN[L[N[LYLYLWN]N[N]LY@EJQN]JULYN]LWN]N[LYN[LWJYP]LYLYN[N]JWLWN]P]LWLYLYN[JUDKHQLWN[NYJWN[P[LWLYNWLYNYN[P[LUNYNYNWN]PWLWP[LUNWNY?ANUP_@LSPYNYFMFKNWP[NWPYLWP[LUNYP[PYLULU@EPYPYJUPYPYLWP[PYNYn@kAPYNWLYNWR[NYLUNYPYNYNWJQ@ENWPYNYNWNYNYJOBINW@ALWPYNY^q@NWNYPYJQBENY@CLUPYJS@CNWBGJQJODINYLUP[NYNWP[NYPYNYNWNWP[LUNYP[NWNYLUP[P[LUPYZm@@CNWBELSNYNYPYNWN[NU?ANWFIHQNWNWNYLUNY@ANWNYNWP[P[LU^q@^o@P]LSN[R[NWLWP[LUP[NWNYNYNWP[NWNWLWPYNYNWP[NWNYPYNWLWP[NWNWNYP[NWNYNWNYNYPYLUNWP]PWNYLWNWNYNWPYNYNYPYNYLUPYN[PY\\o@PYNYP[LSNYNWP[^q@PYFMFMNWNWNWP[P[LUDIJSHOBEP[LSP[LUP[NWNYNYNWNYP[LUJQDKNWLWFIHOLQ`@s@p@iAFIHOP[LW@AN[LUNWP[`@s@?ALUP[LUNWHOFKLWPYPYBGHOPYLWNWNYNW@CLUR]LUP[NYNYJODILWNWPYLUP[NYHODGNW@CLUHMTc@PYBGP[HMDIPYLWDIHMNYNWBCLWPYLS?ARYNWHMDIPWPYDGJONURYNSHKHMPWNSRYPSPWTWPUPWPSTWPSRWPSVYLOTURUPQRUTWTUNOVWPQDGLMLMDERS@APSHGJMLODCRSRURSPQ@Cf@g@LMVYRSRSVYRSRSPSPQBAPSRURSRSRSVWPSRSRSRSVWPQRSRSPSRSTURUTURSFIFETWRSTURSRSNQ@ABCPQRSRSPSTURURQTWPQRSPSBCPQDENOd@g@BARUPSRSRSRSVWPSPQDCNQHKJIPSTURQRUPQ@APSRSRUh@i@HIHIPQ@CPQTURUTSRUPQRUTSRUTUNQZ[LMJM\\]l@m@LOPQBCPQTUPQRUTURUPQTULMFGRUNQTUPQRUTUJKDETU@CPQDENOPQRS@APSHIJKNO@ARUDCLOTWRSPQFGLKLODERUTSRUNMBEPQRSRSRURSFGLMRSRU@?PSHGHKTSRURSPQTURUPQNOBCVWNOVWNSTSf@g@VWNQFGLORSRS@APQRSPSRSRSLMFIRSRSTUPSTSPSTUNQTUTURUPQTUPSTSRUTSPUTSFGJMRSRSHKHGRUVWFGHIRULMFGNONONOHKTUPQTWRSRSPQTWf@g@x@{@VWPQ@ARSRUJIFIRSRSRSRSBE~CcDDCRURSTURURSRUPORURSTWPORUTUHILMNQTSRWRSPOBENORUTSRUNODENQDCNORUJKFGTURSPQBEPQRS@ANO?AVUPS@ARS@APQPSVWNOFGNOJKBETURSPSVWNQ@?TURUPQTUTUPQRUTSPSTURU@?PQRUNQBARSBENOJKFG@APQJKFITURSDENOPQRS?ARSTULMDETURUFGJKTUNQDCLOTUPQ@ARUTSPSPQBCRUPQTURSRURSLKBERSTUPSTSRURUTURSRSPQRSRUTUTURURSTUNORS@ATUNQRSTURURSTURSRURSRSRSRSPSRS@ARSPSVWRSNQTURSRSTWRSRSRSTWRSRSRSRSTWRS@APSRSRSRSRSRSRSPSRUTSRSPSRURSVWRSRSRSRSRURSRSHKHGBCNQRSTWRSRSBCNORSRSNOPSRSFIRSRSFGJMNMDEPQ@ARUPQTURSRURSf@i@BANQRURSTSRURSRS@APQRUTWRSRSRSRSTUNQVWPQTWRSPQRSTWFGLKLO@A@APSDC`@c@RSBCRSRSRSRSRUPQRUVWRSRSBELMTURSPSTURSRSPSRSVYRSBCNORSNQHIJKRSTWRSRSTUPSRSTURURQf@i@TUPQVWRUNORSVWTULOBCPQRSRUTURSTUPQ@CNOVWRSRSRURURSTUPQTURUPQTWRSJKDERUTSRUPQRSVWPSRUTURSRSRSPSTUPQRSTWRSRSLOlBoBlFoFDELOPORUTUFIJINQBCTSRUPQRSRUVUPSTUPSFGLMLMDERS@APQRSPQ@CRSDELMRSRURSTWRSRSPQJKJKRSTUPSPSTS?ATUPQTWPQRSRSTWRQRWTSPSTUPSTUTSPSRSTUPSRSTUPSVWPSRQPSTWRQTWRSTUPQRSRU@ARSFGHKTUPQTUPQTWRURQPSTUTUPQTURSRURQRUPQTWTSLOFEPSTUPQPSTURSTUPQRU@ANQRSRSTURSRSHKJILOBCRSRSRUTURQTWRURQPSRSTUPSTUPQVWPSRSTURUPQVWPSRSRSTUPQRUTURSRSRURSTUPQTURURSRSRSPQBERQPSTURSLOBCTUTUPQl@o@NO^a@Z[RURQVWNQRSTURSPSVWPQPSVUPSRSTURURSRSRURSTURSRSRUf@g@TUNQh@i@RSRURSRSRSDGLMTURSRURSRSPQTWRSRSTURSRURSRSRSRUTURURQRSBCPSPQPQBCPSRQTWRSPSHIJKNOVWPQRUTUTURSPSRQPSJKJKTUPSRSRSTWPQTSFIJIPUTSRSTWRSPQRSRURSRURSTSPSTULOBCTURSTWTSNQVURURSRSRURSRSRUTSLM~@cA`AcAPONQPQRUVUd@g@NOBCRSRSTWNQVWz@}@^]DGRQPSTUx@y@FIPSTUTSRUPQRSRURQTWTUPQRUTSPSRURSTURSRUTSPSRSTURUPQRSTURSTURSPSRSPSVWRSRSPQFGLMNQTUTURSNQBATUPSJKHIPQ@ARSRSJMFGPQ@ATURURSPQVWPQPSTURSTURUPQVWPQTUPSTUPQTWPQTUTUPQRUTSRUPSRQTWz@{@TUPSTURSNQVUPSTUTUNQVUPSPQVWPSRSTURURSRSRSPQTWTU@ANORSz@}@RSTURUPQTURSBENMJMDETUPSVURUPQRURSTURSTURSPSTUPSTURQTWRSPQRUVURUPQRSRURSRSTUPQTURSRURSPQRSRSRUTSTWPQRURSRSRSTUPQ?ATSRURSRURSTUPQTURSTUPSTURSPSTURSFGJKRURSPQVWRUPQRSTUPQVWPQTURURSPSTSPSTURQRURSTULMFGPSRSTUPSTUPQTUFGJKRWRQTWPQVWPSTUPQRUTURSPSVWRSPQTUPSRSTWPQTURUPQ@APQTWTSPSTSNQTUPSRSTURSPQTWTUNOVWRSPSRSTURULMRSRSTW@?RUTSNSTS@CNMJMHGPSTURSTUTUTUPQRSTURSRQNOvAuARSRSRSRSRQ|@{@RSTSRSTSRSRQRSf@e@TSRQTUTSf@e@NOZYPQTSPQXWRSRQRSRQTSRSTUPQTSTSPSTSRQh@g@TSRSRSRQTSTSRSRSTSRSTSTURORSHIJIRSRQrAoAVUPQTSTURSRQRQVURQTUPOTURSTQTUTURQTUPOTSh@g@RSTSRSVSFGJKNOBCTSNOVWPOTSTUTSPQRSVUPORSRSVURQNOXWRSTU`@_@DERQRS@ARQTUTQTUPQTSRSh@g@RQTURQVURSRSTQRSTSRSRSVSRSLMDCTUNOBCTSRSPQTSVURQRQTUPQTSTSRQTUPQTSTSTUPQtAoARQRSTSRSRSVUPQTQVWNOTSTSv@u@r@o@\\]NMl@m@FEHIPOf@c@p@o@VW`B{A\\[JM^]hAcAHIJK\\]NMl@k@NMTUf@c@PQj@i@HIx@u@p@o@b@a@LMJI|@y@JK`@_@p@m@FGJKHIr@o@z@y@n@k@j@i@l@k@|@{@`@]FITUTSZY\\[TSHI`@_@Z[ZW\\]b@a@p@o@RQfBaBRSd@c@b@c@\\[pAkAXY^]ZYt@q@PQbA_Ax@u@VWVUNOVWtHeHpCkCrCkCd@c@XUh@g@XWNOvBqB~@y@bA_Aj@e@d@c@XU~BqBh@e@h@c@j@c@\\Y`@[z@q@bAw@lEeDlDiCTQRQJGt@m@VSh@a@TQNKZWj@c@h@a@vAgAXSlA_AxAgAtB_BzC_C|AkAnAaAxC{BXUh@a@~BgB`@[`@YlByAh@c@bE}CXUVSPMTSTQTOl@e@TSVQRO`Au@j@e@d@[ZU@APOVSpAcAj@a@l@e@f@_@XSROdAw@TQ~@s@bAs@TQVQVQ\\Wv@k@n@c@vAeApBsA|@m@hAw@xAaAj@c@l@_@h@_@dAs@LK`@W`Aq@l@a@ROVQTOPMZSROTOVQ`C_BTOTMVOVQXQROVQTQTOXSLK\\UTQTQRMXSxAaATQTMLKHGRMVQnBsAZSf@_@j@_@bAq@l@a@TQl@_@`As@\\UhBmA~@q@n@c@nAy@dBkAbEsCn@c@lEwC`DyBjIwF`BiAdBkAtDgCtAaApDcC|AeAh@_@hCeBzAcAdAs@BC`CaBxCsBdCcBbFiDvByAdBiApA}@lHaF`K}GzGuE~HkF`As@dCcBZU^Uz@m@zEcDjD_Cp@g@l@a@VQbAq@dBkA^Wp@c@tAcAlAy@bCaBhBkAfCeBtAcAb@YTQTMXShIsF`C_B`Ao@jDcCbEqCfH{Ef@]xBwAbAu@xDkCdD{BvCkBnCmBrA}@z@o@nAy@x@k@tE_DdAs@l@c@|B{An@e@|B}AvA_ArA}@bAo@rBwA|AeA`BiA|AeAbAs@nA{@zAcAx@k@bAq@h@_@xAaAHIpA{@\\U\\W^W\\U\\W\\U@?pE}ClBmAbCaBp@c@pA}@dAs@p@e@~AiAvBwA`Ao@BCz@k@`Aq@tA}@\\WzAcAl@a@jA{@FCxB{AvCqBvAaA\\WbFiDrA}@tDiCr@c@ZU`@WNKrBsA|@o@zAcAf@]r@g@z@m@^U`@[bBgAnA{@pA}@n@a@rBuAj@a@|DkC`CaBf@a@dBgAvAaAd@[vEcDpBsAVORQNKVQ^WjEwChAw@h@_@VOVQTOTOROn@e@rBsApAy@zAeAd@]rA_ApCmBbBiAlBqAhH_FbFeD`Aq@XQh@_@h@_@^WVQROXQRMn@c@ROXQh@_@^Uf@]l@_@LI@Al@c@\\Uf@]\\UROf@]p@g@JGh@_@d@[l@c@r@c@@ARMb@Yh@_@fAu@x@k@h@]fCeBtA_AjAy@b@YdAq@b@[lCgB~B_Bh@_@z@k@d@YVQBCXSRMTODCv@i@r@e@VQf@]ZUl@a@TQLI^WTQj@_@JIJGTQVOTOVQFELITOTQTOl@a@VQTONKFETQXQROxAaAVQj@a@@ATOTQVQTOLIx@i@DCLKBCRMTM`Aq@n@a@bAs@t@i@LGbAu@pBsAl@a@PMBAVQVOvAcAVOTQVOTQ@ATObAq@fCeBVQTQTMXSl@a@bAs@pBsATOl@a@j@_@VQROXSRMZStA_AfAs@PMVQTQVOTOTOVQTQXQj@a@j@a@ZSPKVQHGJITODCPMbAq@TQl@_@VQTOTQTQZSTORMTOVQVQTO?AVQHGFEBAj@_@VQDENIVQXSPMhFmDxFyDfMsIdS_N^Wz_@mWNMj@_@PKBCHENMDCHE@AtI_G~B}AHGJIPMTOZSTOROVQTOVQTOTOVQTOXSTOROXQTOVQROXQTQVQRMTOTOZUROVOj@_@TQTOXQROXSTOTOTOVQTQTMXS`Aq@TOTOXSTOVQTOTQTOTOTOVQXQROVQTOTOVQTOXSRMVQTQVORMXSVQ`Ao@dCeB|AeAtA_A\\U|@o@^U\\U`JgGzCuBfCcBl@a@TObAs@TOn@c@l@a@j@_@JI`@YNIFETQTOVQRMVQVQTOTOb@YPMVQPMRMROf@]`@WPMhCgBRMp@c@zAeAl@a@j@_@zCsBZUz@k@r@g@n@a@`@Yh@_@b@Yj@a@VOJIjD_Ch@]`Aq@vBwAfCcBbAs@l@a@rA{@r@e@xAaA`DyBxA_AJGdBiAdAq@n@e@fCeBfCeB^WfNoJhOeK^WxAcATOTOXQdCcBhH}ERMxFyD~AgARMTQTOl@a@VQj@_@hCeBTOTQTOLIHGTOXSJGFEBCRMTOTOVQVQVQTODEf@[TOTOf@]\\Wl@_@lBqA\\UNKXQl@c@n@a@\\WlCgBJIFEh@]\\WzAcAJIRM|AcA~CwBt@g@`@YdAs@nA{@JIj@_@TO`FgD|@m@v@i@LIZSzB{ABCdDyBVQl@a@dCcBj@_@l@a@dAs@|@m@hAw@\\UlAy@rE}CdCcBzDkCbAs@|CsBj@a@@?xFyDdAs@pBsAr@g@hBmAhCgBfBkAFEzAcA^WLITQTOl@a@VORO@ATOVQTOVQTOTQrA{@FEVQTOTQTOVQTODCNKVQVQTOTQVQTOVOVQTOTQVOTQTOVQVQROVOVQTOTQVOTQVQHEJIPMBA@ATORMPMVQFCLKLK^UVQDENITOTOTQTOLI\\UVQTOVQh@_@XQPMVQVO`@Y^WNMBARKPM\\WVOjAs@~@s@NK@APM`Aq@VQdAq@ROVQPKhBmAjD}Bb@[xCsBf@[f@]~AgAjBoA\\UFEb@[bAu@z@o@r@k@v@m@@An@g@b@_@FE^[^[RQ`@]r@o@RQXWv@u@d@c@TSj@i@h@g@RUNMv@u@~FuFh@g@Z[b@_@|@{@?Av@s@t@s@f@e@JK^_@\\YnBmBBCDCn@m@^_@HIPOVWb@_@TW^[`@a@RQRSNOj@g@DE@ARSFGRSDE^[BEbA_Ap@o@RSXY@AXWjFaFp@o@j@i@jAgANOPOjCgCVULMVUBCt@s@PQTUf@c@f@g@VUj@k@~CwCd@e@`A}@rAqAf@c@`A_AZ[vDoDf@e@nDgD~A}At@s@x@w@HGf@e@VW|@y@VWv@s@h@k@h@e@^_@XYJI^]d@e@TSt@s@LMHIJKJKLMFEPQ\\YTU^]|@}@n@k@vAsATWTSRS\\[LMLMHIBCLMh@g@f@e@RSLKTUh@g@n@m@NOf@e@TS|AyAtCmCDEt@s@^_@t@q@dBaBf@e@h@g@NOZYh@e@f@g@^_@Z[POTSl@k@d@c@^]DEFG`@a@h@e@VWLKRSTSTUPQTSRQ@CPQRSTQRSRSTSRSTSPQTSf@e@RSTSRSRSLKX[RSTSPSRSRQHIHITUPSTSRSRSPSTUd@g@f@i@`@c@XYRURSPSRURSRURURSPURUd@i@LMX]RSPSPSRURURUd@i@RSRURUd@i@PSRURSRURUPSRUPSRUd@i@TUPUd@g@RUXY`@e@PURSPSVYNORUPURURSd@k@RSRSPURUf@i@b@g@TWJMDERSf@k@v@}@pByBv@}@fAoAr@w@DERUbAkAr@w@h@m@BEz@_ATWxAcBfCqCl@o@|LeNx@}@b@g@TWPSd@i@TURSd@i@TWPSd@i@nAuAx@_AtEgFhCwCJMPSRURSPURSRUPSRURURSPUTWb@e@d@i@RURUtB}Bv@_AfCsCx@}@f@k@PSRSPUTUPSd@i@z@_APSFI\\_@Z]JMJMJMNQr@u@\\a@PSNQNONQNQ\\a@RQPSLQ\\_@RSX]l@q@VWPSRUPUbBiBPUrB}BPQFGNQRUPSnAuAPSRUf@i@RUv@{@FIdF{FlCyC^a@~S{Uz@aAjAqAzCiDlHgInD_EjD{DvEkF~AgBtDeEhBqBvAaBLOfBmBnAwAfLkMb@g@HKvCcDnC}CrDaErGkH|BkCRS^c@TWj@m@VYl@s@^a@b@e@j@q@fAoAx@}@RUf@i@LOp@w@fAmA|@aAnC}CxBcCzCiDhAoAp@u@`AgAhBqBdAmAlCyCNQnC}CjE{ErCaD~AeBX]PSpOaQ~JaLpC{CfBoBv@_AX[^a@VY`CmCpC}Ct@{@t@y@tB}Bt@{@X[bAiAt@{@vA}ALOJKv@}@t@y@d@g@BENQFG~@eAVYHKLMLOb@g@l@o@PURSPURSRURWRUPUTWPUPSPURWPURWRWPWd@m@NUPSRYPUNUT[NUNUPWd@o@t@iANUPYJMTa@PUP[FGDGBExHqLVa@PWPWb@o@LUPWPWNUPWNWr@gAPWNUPWNSP[PWPWPYt@iA`@m@NWPW`@o@PWPWPYPWNWb@q@PWPWNWPWPWPW`@o@PWPWR]LSPWPWPWNUb@q@PWPWNWPYPUPYNWPWPW`@o@PWPWPWPYPWNWPWPWPWNWPWPWNWPYPUPYb@o@NWPWPWb@o@NWPYPU`@o@b@q@PWNWPWR[NUNUPYPUPYNWtB}CXc@PYPYNWPWPWb@q@`@o@LQPUNYb@o@PYPWNWPWPWf@u@r@gArAsBR[b@q@b@o@`@o@^i@T]DIV_@?AT[\\k@T]b@o@`@o@PYPWPWNWb@o@\\i@PWT]PY\\i@b@o@PWNWb@o@b@q@NWPWb@o@`@o@b@o@NWPYFIHMPWPWNWPWT]LQT]\\k@BCR[NSJSb@o@b@q@NUPWPWNWPYPWPWPWNWt@gA@APYb@q@PWPWPW`@o@\\k@b@o@r@gAPWPWPWNYBCLSb@o@PWNWPWb@o@NWPWPY@ANUFKHKPW`@o@PYPWNWPWPWPWV_@LUPWp@cALSfF_Ivc@qq@dMqRh@y@jAgB`@o@R[|A_Cl@_AnByCRYhAgBpAoBj@}@Va@hBmCtD{FPWzA_CzEkHfAeBVa@vNsT~EwHRWPYNU`@o@PWPWPY`@m@PYR[NSPY`@m@PWNWPWFKHMPWPWPWr@iAPUPY`@m@PYNWPWPWPWPWNWPWPWPWNWPWPW@CNU`@o@PWRYNSNWPYd@s@V_@PWnAmBT_@n@aALSRYPYNWPWXa@FIb@q@b@q@PWh@y@HMLSd@u@Zc@Xc@PW`@q@PUPWPWDKPWlCaE`@o@~@uAJQpDuFBEV_@nCeEn@aAR[Xa@pCiEvBcDfAcBl@_ApFmIpDqFlAiBrCmEnB{CfCwD`Q{WjAiBxIyM`@m@Va@dDaFfCyDfJkNh@y@^i@R[LS`AyA@CnAkB`QuWV_@?AT[@AJOz@qA?A~@wAPWPWx@mAr@eADIp@cAxA{BPWr@gAj@{@BCzBgDVa@fBmC@C\\i@~AaCpDqF\\i@xCqENUR[^k@b@q@\\g@BEb@q@dA_Bb@m@bA}APYRYNUb@q@NURYNUb@o@PYNUd@s@NS`@o@RYNUPYNUb@q@DEV_@BGRYT]Xc@R[@?`@m@d@u@FIT]PWPYR[NUPWr@eANWBCd@s@Xe@^i@DG^k@b@o@b@q@PYNSdA_BR[p@cABEBCJOPYf@u@d@s@`@m@NUT]p@cA@CPUDIHMNUNUR[NUh@w@Va@jBsCnAkBPWHMb@o@LQFKbA{Ap@eAx@mA^i@bA}AV_@JO@AHMBEj@y@rAsBn@aAPWj@y@h@{@DEDG@CBCl@_ArAqB@CJOz@qAT[LSHMpAoBd@s@JO`A{Av@mAnAoBLQj@}@d@s@l@aAVa@LSHKDGPYV_@Xc@bBkCjBuCBEn@_A?AV_@DIxA{B|DgGfBmCNU`@q@`@m@@CBC`A{AxCuEfBmCbA_BhC_E|BmD~@wAjAiBJMzBoD|AaCx@oAt@kAV_@|AcCdAaBp@cAzCyEh@w@nB{CJQFINWPUP[NSRYNWNUPYNUPYNUPWPWPYNUPWPYNUPWPWNWPYp@cAPYPWNWPWPWNWPWPWNWPWNURYNWPWNW`@o@^i@Va@FKZg@\\g@`@m@PYNUPY`@m@`@o@PWNWPW`@o@NWRYNWR[\\k@PWNWNUR[LSPWPYPYPWNWNUPYLUHKHMNUP[NUPWhBuCdDiFPYHMFKNS?CPUNWPWNWNUR[`@o@PYLSR[NUPYNUPYPWNWNUNUPY^m@@CNUFIHMPYr@gA`@q@NUNUPYPWNWNU`@m@NYt@iAPYFKFINWb@q@NW`@o@hAgBn@aA^m@NWPYb@q@LS@ANUfCaEb@q@NUNYPWRYLUp@gAPWPWNWPY`@m@`@q@NUPWNWT]LUNUPWNWRY^m@bA_BPWNWr@gAbA_BR[JQT]NUNWPYNUNUPYRYLUPWr@iAPYNWPUNWPWPYNUJQbBkCv@qA\\i@^m@h@y@NWP[NUPUR]`BgCd@w@b@s@x@qAh@{@dAaBLSlAmBj@}@R]T]n@cA^k@Zg@HMNWT_@LQNULQ@EPWPYPW\\k@BENUPWTa@|@uANWPWNUPYNWRYNULSBGNQPYNWJOhIsMPWNUr@gA`@q@NWV_@Zg@PYNU`@o@`@q@PWPWrAwBPWPWNWPWNWPYNWPUbA_Br@iA`@o@PYDIj@{@PY^m@PYPWNWRYLSPYNWPWPWR]LQNYPUNWPYbA_BPWNWPWbAaBPUNWPYPUNWPYf@w@R]v@mAfAcBPYNUNWPWNWPWPYNW`@o@PWNWNURYNWPYNUPYNWPWNWPWPWNWPYNUPWNWPYLQBENWBCJQPYPWNUPWNWPWPYNWNUNUP[PWPWbAaBr@iAtAwB`@m@NWr@gANYbA}APY`@o@NWPWNWPWPWLURYNWPWNWPWPWNWHMh@{@NWPWPWPYDGHMPYNWNWPUNWNWFIJQLQR[j@_ADGPYPWNWPUNYNUNUPYPWPWNYd@s@PWNWPWPYNUPYNWNUPYPWNWPUJQBCb@s@NW`@o@PWNWPW`@o@PYPW`@o@PWNWPYPWPWNUNWPYPWNW`@o@R[NWNSP[NUPW^m@DGLQHODGPW?APWBGJOPWNWPYPWNUNYPWr@gAPYNWPWPWLUPYPWPWNWPWNWPWPWNWPWPYNWPWNUNWPWPYNWPUNWPWNWNW@ANUDGJONYPUPYNWPWNWPWNWPWNUb@s@NUPYNWPWPWNWPWNWPWNWPYNUPYPWNUPYNWPWPYNUDIJOPWNWPWNWPWPWNWPYNUPYPWNWPWNWPWPYNUR[LSPYNWPWNUR[NUNWRYLUPYPWPWNWPWNWPWNWPWNWPWPWNWPYPWNUPYNWPWPWNYPWNUPYNUPYPWNWPWNWNURYNWPYNUPWNYPWNUR[NUPYLSRYNWNWNUR[PWNWPWVa@HMPW`@o@LSBCPY@CLQPWPW`@m@PWJODGPYPUPWNUPWPWPWPUPWJQDGPUPURYNUPWPWPUNUJOLONUPWPURWNWPUNSRYHKZe@`@i@PWRYNSPWRWNSRYNUPWPUPWNSRYNST[NUPURYPUPWNSRYPWPUPUNWRWNUd@m@PYPUPUPWPWPUNURYPUlAeBZc@zAuBRWNUPU`@k@T[NUHIHMPWPUPWNURWPUPYPUPWX_@HMRWNUBCLSHKFKPSPWNURWPW@ANSPWHKHMPUPWPWPUPULSf@q@LQJMR[T[FIFIPWPWJMJONUPURYNSPWRWPWPWPWDEJOPUPWRWNUPWPWPURYLQ@CPURWNWPUPURYNUPUPURYPUPURWPWPSPWRUPWPSRWPUPSRWBERULONSTWPUPSRUHIHMf@m@PQPUHKJIPUHKTUDGRUHIr@u@vA_BPQ\\_@l@q@bAiAfBiBnAwAPQdCmCHIh@k@vCcDlBuBd@i@t@y@HIn@q@HKRSNQBCRURSDGLMPSRUBANQRSPS~@cANOf@k@`@c@b@e@n@s@vJoK`BgBjEyELMrGeHHIX]VWrB{BRUTURUNO@CRUDCLORSTWPSRUf@g@PURSRURURSRSRUPSTUPURQRUPSTWPSRSRURURSRURSRU?ARQFIHIRURURSJKX]BANSFELOPSRSRURUPQTWPSTURSPURSRURURSPSTUPSRUTUPSRURSLMDGRS?ARSRUPSRSRSRURURUPSRSTUPSRURSPSh@k@HKHKr@u@fAkAbAgA~@cANQh@m@hAkAHKr@w@hAoAZ[NQ\\_@^a@\\_@RUd@g@n@s@xBaCv@y@pJkKj@m@HK@ADEp@s@hDsDxA_Bf@i@V[DCPQp@u@FG`@c@DEh@m@t@w@`@c@t@y@rC}CHKDELMBELMDEPSRSPSLODEPQZ[f@k@p@u@^c@^_@j@o@bCiClBuBl@q@d@g@f@i@z@_A|@aAx@}@l@q@t@w@PSdAiARUDGLKh@m@fAkApAwAFGTWr@w@\\_@r@u@@Aj@m@t@y@@A\\_@TWVYz@}@X[j@o@j@m@`@c@z@aAf@g@z@_Ar@w@`@e@Z]t@y@pAuAh@m@n@q@~@aAb@g@rAwAf@i@f@k@rAwAlBwB^_@Z]JKx@}@@Al@q@|@aA^a@FI`@a@dCoCfAkAt@w@f@k@j@m@LOh@k@z@_Ap@s@^c@t@w@\\_@Z_@BC`@a@xA_BvBaCd@e@xA_BzBcCh@k@lBwBnKgLfBoBtAyAlAsAfAkAVYNQRUPSRUBANQRURSnAuAh@k@PQx@_Ah@i@@CNOTUPUTUd@g@z@_Ah@k@PSRUx@}@RSbBkBz@_Ah@k@PSRSd@g@RURUh@i@nAuA|AcBx@}@XYRUTUz@_ANQTUPSTWRSJMdEsEpC{ClAsAfAkAp@u@f@i@d@g@RUTWNOV[TSPURSf@i@RUf@g@RUf@i@TW`@c@VYpAuARUb@g@TUf@i@d@g@h@k@PSRURURSnAuA|@_APSHIX[BCd@g@RUPQTW|@_ANQRUBCPQTUJMPQTUh@m@`@c@XYd@i@TURURURUb@e@nAsAz@_Az@_Af@i@f@i@PSFI\\_@h@k@RUPQRWRUTUPSRURSTWRURSRURSRURSRURUf@i@bBiBPSf@i@f@i@RSPSTUJMHILORUTURUh@k@TUz@_Ah@k@xA_Bj@o@PQx@}@vA}A`CiCRSz@_ARWBAPSFId@g@^_@RURULM`AgAZ[h@m@bAgA`AeAJK^c@JKLMr@w@\\a@p@s@JKvB_CPSd@g@VYx@}@h@k@VWbCmClAsAf@g@bAgArEaFX[t@w@BEVWRU^_@f@k@f@i@f@i@PSRSh@k@lAsARSj@m@d@g@PSTUPSPSTUt@w@LOx@}@f@i@RURURURURUPSf@k@TU^e@j@o@JMdD{DRUPUh@o@PQNQ~AkBTUPSh@o@Z]LONORWfCuCPQ@CPSRURSz@cARSf@k@b@g@RURWPSRURUPSdCqCV[RUd@i@f@k@RUPUVYPSPS|@aAJMRWRSpEiFhFaGvDmExBcCX]zDmEr@y@\\_@fBsBt@{@X[bAkAd@i@Z]X]X]z@_ARWdCsCRUb@g@TY`AgAt@{@BETWb@g@\\_@^c@HIb@g@DGLORURURSDI^a@TWNQRURUVYr@y@RURULOBCPUTWRURUVWX]TWZ_@RUlAuA^a@FIJKrA}APURURSRWd@g@RWPQTWRW|AgBf@k@d@i@RUf@k@RUPSRURU`@e@DGPSf@i@d@k@d@i@HIHKPSTWRSTY`@e@fBqB`@e@X[`@e@`@e@TWTWNQTWd@i@lAsAv@{@RUZ_@^a@x@_ATUZa@JKPQx@cATUNSf@k@RUdCuCRURUNQV[NQdBmBd@m@JKFGPSPUTWPSBCPSRUPSZ_@r@y@NQTWr@y@d@i@RWTUf@k@PSPUTUPURUd@i@d@i@~AiBNQf@i@RU^c@FI~CoDp@w@dAmA`@e@h@o@PQPUNOz@cAr@w@LSLMd@g@v@_Ab@g@VYjAsA`H_IRUTW~AiB~AkBTWhCwChFaG|BkCpB{BPUb@e@f@k@RWx@_AlAuAZ_@JMLOJKNQPSRUNQBEPQBCDEn@w@d@g@z@cAv@}@TWNOX]b@g@|AiBRUh@m@PQRUd@i@RWzCkDRUPSRUTWd@i@b@g@NOFIPSv@_AVWTWNQRUPURURSRURUd@i@x@_ARUTWPUx@}@f@m@RU|AeBRWRSPSRURURUPUTUPUPSVWNSTURUPSRWPQLODGRURSPURSRURUPUTU@CNQPSPQ@CRUTURU?APSRURUd@i@RUb@g@TYPSTUPSPURUDCLQRSPUPSTUDGLMPURSRUPUTUPURURUNQRSPURURURSRUh@o@NQRSRUTWtA_B^a@PSf@k@d@i@PURSd@k@h@k@x@}@DGxAaBRW~AiBrGqHx@_AV[`@c@bAmAVYv@}@j@q@v@_ALOf@k@f@k@PSTWPQx@aAjAuATWNSRURURURUPSTWb@e@TWx@_AFGp@y@RSjAsADELOTWPSRUpAyAPSLOVYNQnAwArBaCz@aAz@aArBaC`BkBPUbBmBv@_ARUb@e@NQj@q@`BkBNQTYPQNQDETWb@g@v@}@d@i@z@cARS\\a@X[VY@Cb@e@PS?ATWDCHMh@m@Z[FKPQz@cAnAwAd@i@RSPURUh@m@FGbAkAlAuAf@i@d@i@RW@ANQJKFGRWRUPSTUPU|CiDd@k@|@aAd@g@RUd@k@RUPSRSRWr@u@`AiARUPUf@k@RSd@i@f@m@v@}@TWTWNQRURUx@_APSTUPUPSh@k@RUPUf@i@PSf@k@f@k@PURURSd@i@PUTUPSRWRSPUd@i@TWv@}@RUPUTULQ@AJKFIRURURUPSRUTWb@g@TURWRSPUPQf@k@\\a@^c@X[HIRURURSPURURURURUNQ@ARWRSRUHKFIRURURURSFIJKRWPSRSRURWPSRURSRUPSRSPUNOBERSRURURURSPUTUPSRUFEJMRURUPSRSX[X[FGTWPSRSRULMPSRUTWRSTWRUTWf@i@RURSRURURSRURURS~@eANO`BgBRUTWd@g@X[LO\\_@HGPSPSTUd@k@RSRU~AgBVWRSRUx@}@FIJMRSRSHK\\_@RSRUPSLOFEPURSRURURSf@i@PSJMHIRSPURSRURURSPSh@i@PURURSRSRWNMBEb@e@RURURSRURURSPURSRUlAqABCPURSNQHK`FoFxCeDlE{EX[jAmAnD_EHKfBoB`BiBjAmAX]\\_@`@c@z@_Ad@i@RSTWx@{@f@i@f@k@d@g@j@m@PSPSTURUPSRSTWRSRUPSRUPSVWNQTWPQRSX]LOTURSPQRWRSh@m@FGr@w@@ALOJKFITSRUPSLODENQPQTUTWPSRSRUPSTUHIHIRUTUPURSTUPSRSRUTURUDEJKRUTUNQRWRSRUTUPSRUPQRUTWRURSPSRURSPURSTWRUPQJMHIr@u@BETYRSTWJKv@{@r@w@@Cb@e@h@k@NQn@q@DEp@s@?AV[@ALKX[TWlAsAlAsAv@{@VYTUnAsAPUf@k@~@cALK\\a@r@w@LMt@w@BCb@g@RSPS`@e@p@s@TWl@o@\\_@JMb@e@HK\\_@BC`@c@l@o@NQf@k@f@k@X[FGr@w@^a@\\_@RUp@u@BCr@u@`@c@b@g@d@g@BCNQjCuCDE`@c@b@e@|AcBJMd@g@FIFGPS@?h@m@NQPSRSTWPQLOBCTWPSTWPQRURSRUf@i@x@}@RUX[v@{@@ARUh@k@VWPUHIJKl@q@RURSRUTUPSRURSRURURS@APSRURSRURSPUTURSRUNQf@i@TWPQRWRSRURSRURUPSf@g@PURSRSTYRSPSTURUPSRURSRURSPSRSNQPSLMDGRS@ANQTURUNOVYRURSRURSRSRURSRUTSRSRURSRSRSRQTURSTSRSTSRSRSTSRSTSTSRQRSTSTSRQTSRQTSRSTSTQRSRSVSRQTSRQRSRQj@g@RSj@g@TSf@c@RQTSVUPOTSTULMVSPQVURQTSRQRSRQVURQRQVUPOTSTSRQFIJIPOBCRQTUTQTSPOTSTUTQRSFEJKTSTSh@e@h@e@TSRQTSRQRQVURSRQTSPQf@a@f@c@BCNMTS~@y@RSTSTSh@g@RQj@e@RSh@e@TULKd@a@h@g@\\[JIFGLKPOVWDCNMRSRQNMRQRSRQVURSTSRQRSTSRUf@e@TSRSRURQRURSHIFIRS@ATUPSRURURSRUf@k@PSRUd@k@RWPURUd@m@d@m@PSPWPSRWFIHMRUPWPSRYNSx@eAd@m@b@k@PURWPURUPUPUBELQJKFKPURWPSPURWPWRUPWPURUPWPURUPUPWRUPUPUPWRUd@m@PURWPW`@i@RWDGJKRWNUPURWPUPSRYPURWPURW`@i@TYPSPUPURWFIn@y@PURWRWb@m@RUPUNSTYPWNQRYRUPURWNSRWPUNSRWPUBCNQRWRWHI^a@FIDEDGDEDEFGJKJKLMDC^_@JIFGFEDELKDCRQDEFEDEFEDCDEFEDEFEDCFEDEDEFCDEFEDCLKLIFERMTOj@]NK\\SBAJGJGJEDCDCFCBCJEPKLGDCJEBCFCNIJM@ABABAXOVMVMVMJE`@SJEJGfAi@VMHEf@Un@[lG}CtAq@tBeAb@Ud@UPId@UBA~@e@`Ae@TMVMVMTKHELGVMVM@Al@YVMTKXOl@W@AVKVKXMTIZMTIVIVKp@SXIPEBAZK\\KXI\\KJC@A@?NMbB]PELCDAVGv@UpAY~@SdAUn@M|@Sp@OXGZGTGNCxA]\\GDAZGDA\\GHCpAWfASx@SREDA@?fAWjAWPEb@In@OXGVGXGn@OlAWXG`@IrCo@n@MVGXGVGHCNCPEFAZIB?`@KHAFAPE@?`@KNCLCBAFATG@?BA`@I`@KD?~@UHAREf@MLCXG\\IPEt@Q^INCt@QTEXGTGB?jAWtDy@HAb@KJCpBc@NE@?dCi@VGXGXGDAXGVGXGXGVGVGXGZGDAREVGXGVGVGXGXGd@K`@IBAXGf@KJCXGVGXGNEFAXGXGXIr@OTEZIXGhAWTEXGJCNCTGZGLCd@KZI^INE|Be@tBe@b@KPCNE|A]HCdAU\\Gd@KHCTE`@KPCn@OBA`@IJCJCvBc@fAWBA`B]REtA[TGRCTGnAYb@It@Qr@O\\IlAWB?|A]~@UdAUb@IrAYhBa@dDu@FA`B]z@SzA[nBc@fAU|D{@jAWhAWbASn@Ot@QbB]ZIn@OTE^I\\InAY`@ITGPEtAYr@Qp@OXGNCb@Kr@Ot@Qn@MXGJCd@Kp@Or@OVGZGf@KPEbAUVEr@OXIXGVGXGVEHClAW@?TGJCPE`@IHCj@Mb@I@?^Kb@I`@K`@I@A^It@OPE`@IhCk@BA~Bg@v@Q|A]^I@?^IBALCREfBa@b@IdAUhCk@ZGXGXGhAWNEb@IZIDA`@IFAfAWjAWZGt@OfAWTEt@QZGVGn@Op@MZIXGXGTGhAUFCREVGXGLCb@I\\Il@Mp@QPE|@QVGXGJC\\IB?b@K`@ILCTG`@Ih@MZGFCPCFCPCNE@?DATEBAFAPEJCFAVGB?XIFANCZIn@MJCf@KZIXGHCb@Kp@ONEb@KVEf@Kf@MZGfAUf@MvAYZIdAUz@Qb@K`@I`@Kb@IFAFCJARGRETE@?TGnAYFAhAW@?JCREn@OXGXGBAVEDATEREB?VE\\GTETCXED?FANCVCTCTCRAJA\\CTCb@CRAVA^A\\AD?b@A@?D?LAB?B?@?N?J?F?J?B?R?V?B?F?J@V?`@@@?N?R@N?R@^@B?n@@B?P?d@@X?F@L?\\@Z?V@Z@Z?Z@V@V?\\@X@T?lCD^@b@?h@@j@?^?XC`@Cb@GZEVG^GTGFCXKRI@ABANGBA@A@ALGh@[hA{@j@c@j@_@b@YVOl@[HETKHEJEDAd@QHEt@STGPETENCh@IVEb@EF?LA\\CVAX?L?h@?J?d@@n@BjADf@@\\?TAF?D?D?DATA@?VEd@GBAXEDCZG`@MNGVKDCv@c@XSVQVSHIb@c@BCNOPWDGPW\\e@LQRYNSTWl@m@?A^[RMLKTORMDCTMXO`@Q`@OFCb@MLC^IPC\\Gl@GnAIf@CJAb@CfBKv@Aj@CB?dA?zC@d@?fA?z@?f@Ex@IHA|@Sd@M\\M^Oh@Wd@U~@c@VMfAk@PIPIh@STI\\KDAZIf@KHAPCXEv@Ef@A`@Ad@@b@@d@DPBTD^FdARvBf@r@Nb@Hj@FZDTB^@Z@v@ALARCRAnAGtAAj@AlBGvBCh@Ar@Ct@Ed@CZEZEXEf@GVEVE|@OdASxB_@tAU`BU`Fg@r@I~@KjAKd@Gp@IXEXEVEj@KVGb@Mp@Qn@Sd@QXM~@_@`@S^SNINIRMZSf@]f@_@j@c@bAy@p@i@bAw@tC_Cd@a@VUTS`@_@j@m@v@}@r@}@V[@AX]~@kAl@w@`BuB`BsBrAeBf@q@fAiB`@aATg@L[Pk@Lc@J_@HYF]H_@F[He@d@gD?AFg@?ALu@Ly@BQDUBSFW?CDQDQFUBIDQJYFSNe@Pe@JUd@mAx@oBp@eBN_@f@oA`@cADMxAsD\\}@vCmHHUFOP]@EFKHQNWXi@Xc@FMNSZa@\\e@NQJONOPS@ANO@ARSPQPO@AROXWHGFETQVQVONKFETMRKNIHERIZOPIVKr@[^Ml@WXMFEBAt@YTKVKb@SRIVMVMTKTODATOTMTOROTMNMXSTQNMNOHGNMTURQV[JKLOTUV]p@{@NU@AFIz@sAJQzCyE^k@x@sAJOn@cAR[PW\\g@@Et@iAPYr@aAPWPWb@i@f@m@\\c@jAsALMPQNQ`@a@Z[DElAoA|@}@rAsAZ[f@g@NMVS`@_@FG|@}@@Ax@y@TWrAsAPSzA{AnBoBX[Z[Z[d@g@Z[LMLMLMZ[JMLMh@i@LMLMLMf@i@LMh@i@h@i@JMdAeALMX[j@i@Z]`AcAZ[JK^_@Z[`AcAfAgAHITURURSRQRURSDELMLMDERSRSRSPSVUPSJKFGPQTURSTSPQRSLKZYh@g@h@c@PQ@AZUNORQVQPOVSTQROBC\\WHGj@a@b@[FGTOTOHE`@YTODCPMTOROVOd@[DCj@a@XQRMZUPKj@_@ROVONMDCXQRMHG^UXSTOf@[BCTOBARMTORO\\UNKj@_@@ATMHGJGPMn@c@LI^Wj@_@NKDCj@a@h@]@AbAo@j@a@j@_@l@_@j@a@\\SNK`BgAf@]DCn@c@TOTObAq@b@Y\\UTOl@a@TOl@a@bAq@`Ao@`Ao@BAh@_@`Aq@bAo@l@a@j@a@j@_@l@_@j@a@ZS~B}AbAq@j@_@TOTOTOj@_@BCnKcHpIwFxDgCzAaAtA_Ad@YXODCv@_@p@Yr@WFA~@UFALCd@IfAMz@GD?tAC`@@n@Br@Fn@HjATp@Pp@RhAd@z@b@`An@d@^v@r@DDn@p@`@^pAtAvBzBhBpBn@n@j@j@f@f@~@`AfClCJLNN^^LLXZJJNNZ\\l@p@d@d@JLrAtARRtD|DLLLLjBpBz@z@Z\\l@l@`@d@pArARPjAnAZ\\ZZt@x@RRnApAlApATTz@z@j@n@jAlA`@b@d@f@tBxB~@`ADBv@x@lAnAfAhAHHxA|ArCvCzB~Bt@v@fEnENNf@f@JLLN`@b@p@p@^`@^Zb@`@VPLJXTh@^\\Rj@\\l@Xl@V\\N\\LJDr@TRF`@JTFXF`@HNBLB\\Dh@HP@XDX@j@Bb@BT?v@@VAZ?VA\\AVCr@Et@Ir@KVGTEr@QfAYrB{@JE\\QRILGDAVMVOTMj@a@XSXU\\YFGNMTUh@i@d@i@`@e@DGPU@?zAkBPWl@q@d@m@d@m@X]X]X_@X]LMxAiBlA{A\\a@TYX]FI\\c@`@g@hAuALOLOHI~@mATWZ_@PU@At@_Ad@k@PUTYfAqABE`AkAf@o@X_@h@o@NQRWrAaBLOLOV[b@i@X_@HIf@o@jAwANSTYPWPW`@o@JQBEDKR[HQP_@JUP]JYN]JYHU?AJ[JYJ[Lg@`@eB@CJi@Jk@D[F]D]NoADs@JyAFcAPyCJkBJ}AP{CB]?C@G?IBa@Dk@HmA@U@WJeBBa@F{@@OPwCBo@Fy@HwADu@FeANgCZcFFiADq@@GDy@B_@?IBUD{@F_AB[Ba@?I@SB]B_@Fu@Bc@F{@B[@YF{@L_BF_AFw@D{@Dc@Du@HiABa@Da@Bk@Ba@Fk@FaABYBc@B]B_@@MDq@Da@J{ABa@B]B_@Ba@F{@J}ADa@Dk@@]ViDDw@RsC@MLgBF}@Ba@FaAB]B[@W@IB]B_@B]Be@B[@a@B]Bc@BYB_@@[B_@B_@F_ABc@HyABa@B[@K@WBYBg@F_AB[Da@D[BUFi@F_@DYFa@F]F]P{@@EPw@ZoABG^oADMDOL_@JWFQRc@L]HSFMJSHOJUb@y@DILSP[JST[PWT]LQNSFKHKPWHMDIRWFKFIRYLSFGLQLST[LSV]LSPWPUR[BC`CmDRWDINS^i@PWRW`@m@HMXc@d@q@PWLSNSPYDGJQPYLUPYLSR[LWBCLUNUP]^q@JQP]NYNYLWP]LWZm@jCgFP]JS?ANYNYNYLYJSP]NW\\s@NWN[\\q@N[LW@ALW\\q@^s@Zo@NW^u@Tg@Vc@\\s@^s@\\s@l@kANYLUNY\\u@NYNYNYNWZo@N[NWLYNWL[NYHMDINYLY\\q@P[LWFMVe@Xm@P]Xi@Ra@@ALWZm@^w@P[LWz@aB@C|@eB@ETa@NY?ADGh@eAHQfAwBTc@Tc@?AR_@Tc@DILYTc@DINW@C\\s@HMb@{@Te@FMJSHOd@}@N[`@s@\\o@f@}@\\k@@CFKZg@Zi@@An@eAPWj@{@BENSb@q@JOX_@\\e@`@k@d@m@^g@NSd@m@|AkBjAsAbAgAFERUb@e@`@_@TWz@y@hC_CRQHINKTUTQj@g@ZWROl@e@b@]x@m@RMhAw@n@c@VOn@c@~@k@p@a@x@e@NIfBaAf@Uz@e@p@[pAm@x@_@^Q`Bw@lAk@RK`Ac@vAs@hAg@^QTMHC\\OVKJEz@]`@OjA_@NEfA[p@O|@Sb@In@Kl@I@A|AO`@Gt@Et@E`ACf@CbAAfAAnCANAj@?@?tFEfBAb@?nCCrAAxDC|CCrECv@?dA?d@?b@?b@@v@@T@`@?p@BdADnAFH?D@`@Bd@B|AJL@xALrANtD^bAJr@HPBfBPb@Dl@Fb@FdAJdAJfALdAJb@DL@TB@?`@FhBP@?H@VBb@D^Dr@HH@XDfAJhBPD@|@HVBlBRf@FnALzCZ|@JfCV~@Jj@Fb@DD?~@LbAHZDVBZDXBVBh@F|@HRB`@DxBTp@F^D~Gr@@@d@D|@HjAHxBNf@B|@DvBFp@@N@V@hA@Z?f@@fAAj@?P?j@?lACx@AzBI`@AL?bAEdCI^Cl@A|@Ez@C@?v@CdEOdAEP?PAH?j@C~CKRAr@C^CB?b@Ax@CLA~@CvCKt@Cr@CxBIvAEb@AjAG^CTCn@IVCDAh@G`@Ir@MDAJCh@MZIJEHAPG|@[JCHC|@[rAe@j@QbA]fA_@`A[XKxAg@vAg@B?r@YZKd@MNGNEJEj@Oz@[r@W@?JEt@UBA\\M^O^Mp@ULEBA~@[BA@?NGTGBAnAc@nBo@REJCr@WRKTIf@QBA`@OHCd@OHC\\KVIRGXIXIn@SB?TG\\KPEXIt@QTEVGDAPEHCNEXGVGTEBAXGXGVGXGDALE^IRE\\IHCLCXGVGZGVGXIVGB?VIVGVIXIVIXKVIVKXKVKVKVKXMRKVMVKTKVMVKVKTMXMTKVKVMXMRKDAPITKHERIXMTMVKVMVKVMVKVMVKVMTKVKZORITKZOVMTKn@YVMVKVMVKVMn@YVKXMTMXKTMVKVMn@YTKXMVMl@WVMVKXMRKZOTKVMVMVMVOVORMVQTOTQTORODENMTQTSRQTSTSRQROTSTQRSLIFITQRQTSLKFERQRQj@g@RQTQVU~@u@?A|@u@tAmApBaBJKxAoArBeBhEsDJIPOTSBCRORQf@c@VU\\WJKRO\\YBAFEHGHEJIb@YVO`@ULGNIZO\\Ob@QXMVKPGLENGHCNG^OXKNGDAZMTKTKXMRKVMp@a@VORMTOTOVQTSLIDERQx@u@VWb@e@^a@Z_@@ARYTYNUZc@HMLST_@LUFMDGNWHOFMJUDITg@N]FMNc@Xw@@CFQ@EDIFS@CJ]Po@T{@FYJc@Ji@DSDSHi@DWBKHe@@C?CF_@@E@CDYBK@IBKBOJk@He@DUBQBMBOBMJo@Ny@DQJg@R{@FULe@J]HYL[?CL]HWPc@FORc@?CHOFO@CRa@DGHQRa@HONW@CJQHMLQJOPYPUX_@HK@CLORULQDERSRSFGHKVURQ@A@APQTQDEJIl@e@TORMTOVQXORMZO`@SHEXMVM`@QNIFCt@[ZO`@Sf@UZQ|C}A^SLIPKz@o@h@a@HG~@{@HI@AdAiAv@_AFIRYHIPYLS`@m@Vc@n@iAh@_A|AuCFMXg@Ta@JQNWXc@DIHM\\i@JMBCNUb@i@FGZ_@DE@ANOPS@APQDETULKLK\\YROFG@An@e@BAFETONKFEBALGVOTMl@[PGPI\\QJCZMJENEVIVIHEREZIJCPE`@KPCTEh@IHCVC\\ENCPA@?RCTAn@E@?VAH?P?B?F?J?`@A@?j@?V@X?jA@P?d@@j@?Z?b@@T?v@?Z?F?n@AH?L?XAZC@?^CTCr@GPC`@GXEVCBA\\GPEFAVG\\KRGXINEJEVITI@?XKXIXKTIXI?AVIVIVKPGDAXIXKVIJEJEXKVIDAPGjAa@RGBAXKFCNGVGn@UXKJCx@YB?^OPGXIRIb@ONGJCDCFAv@Yh@O\\MFCNEPG@ANGJCTIp@U@Ap@SVINGv@WNGf@ODAh@STI\\KTIRI@AZIVKXI\\MFCHEVINGb@QRKZOB?\\QVOJEXQTO@?HGJGFEPM^WFEVSh@c@ROFGd@e@NODEBAVYHKVWHKV]RWNS@?RYNUDGJQ@CLQPYFKVe@P]LWNYBGVi@\\u@LYLYN[HSHODKN[Zu@JUTg@Vk@Zs@^y@?ALYp@{Ab@_ALY?AJUN[N]Zq@BEh@mA@CVi@Vm@\\_AVo@X{@?A@E@AHY@GFSLa@Pu@FYR}@N}@F]F[Da@F_@NwAJoAFqABy@B_A@y@FaF@e@@y@@e@@]B_@?ADu@@]Dc@Bc@J{@De@@EFi@@GFa@F]F]F]H_@F[H]Ja@HYH]L_@@IVs@Ts@JYHQBIZs@Tg@Ra@N[T_@LWLUZe@V]NWLOBCRW@CLOX]\\_@VYPORSVWDEPMRQRQVQtAeARQVQROVQbAu@^YPOLITSROh@i@VSLMZ]`@e@RUTY@ANSPUXa@HKNWRYLWJOf@}@JUNYBEJSNYn@oA\\o@^s@Tc@l@_A\\k@\\e@Za@b@k@PUHKFIf@k@b@e@TUh@i@TSTSPOROTQTSJIFEVQRO@AROTMJIJGVOXQPKXOTMVMVMPI\\OVMTKVMLGJEVKHEJGXMVKXOHCd@Up@[HCd@U^Qf@UVKXOPI\\OVKTKRKFCRKn@[XKTMXKTMHEJEXMVMVKXMTKDCPIVMn@WTMZMXORILGd@URIVMXMTKXMTKXMTKVMVKVMVMBARIXMVKTMVKVMVMRIBAVMVMTKXMVKVMVIXKVKBATGVIXIr@QVGXGTEVG\\EXEXEVCVCB?ZCZCVAVAZAZ?VAZ?X?B?ZAT?D?PAP?D?X?^?XAX?XAX?H?N?XAZ?X?ZA^?h@AZ?V?ZAZ?ZAV?X?XAZ?X?XAZAR?J?n@An@A^Ah@E\\CZCVAXEZCVETCBAZEZGVEh@KB?\\GZGVGPEFAXGZGdAUZGXGXEXEXCXEXCXCXCZAXCXAP?`@AZ?X?X@Z?Z@T@ZBV@ZBXBXDXBXDPBH@lALlANXBb@Fh@FXBr@JlALPBb@Fr@FH?NB\\@X@l@BZ@Z?Z?X?XAXAZAVA\\AX?n@Ct@Cv@Cr@CXAt@CjAEt@Al@C`@AXAXA\\AXAr@CXAn@Cv@CXAXA\\?p@EZAl@C\\CXCPCb@EXCVEXE`@IRCZGTGZIVGRGFAVIZKTIXMPG\\OVKVMTMp@]TOVMTOVQROXSh@a@TSTQRURQPOTWRUTUPUTYNQPWPUPWBELQPWFKXc@PWPYV]`A}ANWNUPYLQBENUNWNURYNWNW@ANWPWPYLSLODKPWNUPYPWPWNUPYNUPYPWX_@HMPUNSTWRWPSTUPQTUf@c@BCPOTQTSROVSJGHGRQ\\Wl@e@JGRQVSRQVQRQTQTQNMDCRQVSPOVSRQTSPQ@CTSPQRUDELMRUTY?ARWLORYPUNUPYNWPWHQDGNYN[NWN[JWHSDIJWN]HS@EJYL]H[J[Nc@?CZkABEFWJ_@@AVcAXeAJ_@BGDSV_AH[HY^wATw@H[^wAH]J]HWJa@FU@GHW@IHUHYH[Xy@FQPg@L[JUHUDILYLYLUN]PYNYNUP[PYPWPURWNUPUTWPQTY^_@BCb@c@RQNOPM^Yj@a@h@_@RKFEFEXOVOXOf@UJG|@_@PIxD{Av@[n@WrBy@HEn@W~@a@TKb@UXQRKVQZSPMTOLK^YHGHI^YBELKv@w@f@i@f@k@RYPSRWPYNURYZg@PWhAgBBE^m@FIVc@vAwBNWFKFIt@kALS@ADGJQPWNWR[lAmBXc@b@q@^k@`@q@b@q@PWPY`@o@p@eAPWPYPWPWp@iA@?HOT]PWRWPYNUPWd@m@b@k@RWd@k@d@k@d@m@d@k@d@k@RSd@m@PSTWPSRWd@k@JSRUNSFKb@k@LQ@CPURYNURYBGFIDGHO\\m@`AoBXm@JSf@cAN[BEb@aAv@eB\\s@Pa@LYLYNYL[LWf@gADKLWLYLYN[N[JW?ANYL[f@eA@EP]LYLWJU@E\\s@l@sAJU?ALWN]N[LYLYLYFMDKl@oA\\s@f@iAPa@`@{@FON[N[LYN[JW^w@JWHOP_@j@mAN_@Zq@LY`@}@h@iAN[Xo@Zu@\\s@N[DMVg@f@kAJURc@NYLYLYHQn@wANYLY\\w@Zq@Tg@FMHQDKJWTc@JU?AXm@LYBGt@}ABCLUNYJQ?AR]PYHMNSZc@Xa@HKTWNSRUf@i@XY`Ay@HITSTQd@a@VURSPOTSRSj@g@f@c@FGPOVUb@a@RQrAmAdA_Ah@e@l@i@HKp@m@zAqARQh@g@x@s@HIPONMRQRQRQVWTSVURQRQ@Af@e@VWTSj@e@RSRO^YLKVQTQVOPM\\Q\\SLIXM^QNIXMVKRG@AZKXIVIp@Q\\K|@QZEtBYt@IZEZCl@I`@Er@IZEt@In@GPCn@IZEn@Gv@Kr@Ip@IVEXCZEXEVCx@Kl@It@Ij@KB?\\Gb@Kd@K@?p@QVIVIBANGZKZMXMTKd@Ub@SVMFENITMRODATOLKFETOVQ@?TOPMXQPOBAVQROTOTOBARORMHGVQHGXSTMl@a@NMTODCj@a@VQJGJIRMTOh@]VQVQTORMVSVOTORO@?TQRMb@[JGVQHGZURM\\SXSTOPMXQROTOTOVOVQTOh@_@HGLITOHG`@YXStA_A`@WNKf@_@\\ULILIPMJIVOTQTOFE`@WXS^Ud@]TOTOJI\\UZURMROXQh@_@VQTOVQj@_@LK\\SVQROVQd@[DEXQd@]ZSROTO@?l@a@j@a@l@a@ROXSFCJIXQb@YZUTONKZUVOh@_@z@m@^WTOVQVOTQNKLIPKRQVOTQj@_@VQNI\\U`As@VQTORMXQXQFEPMf@[VMLI\\QZMFENGVKZMTIVKRGHCTITGXITG\\I\\GHCPCTEVE@?NCLARCJAJAXE^CD?VA\\CN?ZC^AXAXAj@CBAJ?lAGb@Cb@CJAZERCVEJAh@IVGXEbAUZKXIZKVIRGVKBA\\MHGTI`@Q?AFCLGLGNIRKTORKTQNKJGDCPMPKTQVQRMTOVQJIFENKFETOTQPMZSFEJGVQTOTQTOVQPMLIv@i@RMROTOLKHEXQTQTOTOTQTOTOJIJGTOTOTQVQRMTOHGJIPKDETOVQTOPMBATOTOTQTOVQROVQVOTQTOPKBCTOVQTOTQTOROVQTOTOVQTOTQNIHGNKBCRMTOTQVOTQ\\ULITQVOVQVQROTOj@_@TOLKTOTOROVQVOTQbAq@TQTOROVO`@YNKPMVOHGHGXQTQFCb@[\\Ub@WNKl@[^SDAf@WVMTKXMVMVKVKXKHCJETIZKd@OB?f@O\\KZIXITEn@M\\Ip@Kr@K`@G\\EZERAVCTCZCZCXCF?JAL?NA`@A\\Ar@A\\?L?P?X?N?`@@Z?^@f@@`AFP@PBh@Dd@Dd@Dn@Hj@Hn@J`ALz@LlAPL@RDj@FXDj@HNBZFXBVDxARPDjANlAPTDJ@ZDD@TBF@LBVBj@Hh@HTDRBRDVBdC^VBf@Hn@H`@FTDXDf@Ff@Hb@Ff@F^D^FVBXBB@XBH?L@TBD?X@J@T@Z@X?Z?b@?Z?B?FAN?J?DAVAXAb@Ed@E\\CJAFAPCNCj@INEJAVG@?ZIXG\\KTG`@MXKn@Sd@ORGf@On@Qh@Mb@KRERETGNCZERC\\EVCd@ETCP?\\C\\A`@A`@?b@?h@?^@^@V@XBXB`@Dl@Fh@Dt@JTBR@LBP@^Dt@HB?rAPbEd@B@x@FlAHz@@`@BN?lA?r@At@Ct@EPAXC`AILAPC~@OXGj@K`@I`@Kb@Kd@MRGNGh@Qp@Wl@Yz@a@f@UFELGPI@Ap@_@HGTODEDA\\WFEBCh@_@ZUh@_@pA_AXSb@[x@k@JGDEXSHGLIJITORO\\Wj@a@BABCh@]d@_@BAd@[d@]f@_@XS^[TURONQTUHKJKd@i@JMFGp@{@RWT]bA_BN[NWLWNYLYLYL[LYFORe@^_ATk@LYh@oAJUPa@LYJYL[LYPa@`A_CN[JYRe@f@mALWVo@LYXs@FKTk@Re@Xs@Vm@Ti@L[LWLYHSL[jAsCr@aBr@eBBGTg@DKLYdAgCJWN[HODIFORc@NYNYNYNWTc@Zg@LUPWBELSLQ@CNUDENUFKDGRUPWRYPURWRUDGJKt@aAn@u@JONQPUn@w@JM\\a@PUHKLQHINSNOX_@X_@NQV[z@gAj@q@JOX]NQNSRWDE|BuCj@q@v@aAhAuAPULONUx@cABCRWRSPUPUPURURWb@i@p@{@Z_@DGLM@Cb@g@DENS\\_@VU`@a@XWTSf@_@HGRO`@YXQ@ARMHEFCJIVMVMTMZOl@UVMVKVMr@Yz@_@fAe@dAc@vAm@x@]~@_@@An@Wn@Yr@[j@U~Aq@hAg@bBs@vB_Ap@YfAe@hAe@fAe@`Aa@^OdAe@fAe@NGNGrB}@~@_@rAk@t@]PG`@Ql@Wd@SNG^OFEf@Sx@]TKTKj@Ud@Q`@Qp@WPIXKv@Y\\KXKNGb@MVITIXIXIZKTGRGx@UVGXIjA]l@Qj@OPGxAa@FCTGXIVIv@UTIVKVIVKZKTIXKVIXKXIVKVKXIVKXIXKl@UXIXKXKVIVKt@WhC}@~@[hAa@h@Qr@WPG`@MLE`@MVIPGf@QPGXIXITITGNEhBk@b@O`@MJE\\KTI\\KRILCFCHEHCLETIVILENGTIXIb@OLGZKl@SjAa@VKZKn@UXK@?l@SVIp@SRGbAWLELCd@K`@IXEj@Kr@M^GtCc@fDg@TE~@MtAS|@OrB[p@KZEfAQrB[XETE~@OZGLCt@KnASp@Kb@Gd@GbAQf@I`@GVCn@KFAb@G\\G~B]`AOl@KVEj@Kl@Kf@Kp@QZGRGZIZIn@Qr@SLE`@K^Mh@ONGJCp@SVKREbCw@VIXIXIp@SVIRGDADCREjC{@v@WXKVIt@UTGRGRGd@MFCh@Mt@STG@?VIZIl@SZIBAn@SXKXKXMVKRIPGd@Ud@Sd@STMbB_ArC{A\\SBAr@a@~@g@l@]ZQRKn@_@^Sz@e@hAm@n@_@VMzBoAtC_BfAm@HEd@Wb@WbAi@z@e@DC|CeBHEfCwAb@WXO|BqAlAs@j@]|@i@VOjBmALIn@c@BCTO@A@?BCVQZWFCPMDCBCFEPMHGROBABAzAgA@A\\WBCRMt@k@`@[x@q@fAw@\\WXS@Ab@YRKf@YPKLEf@UVMLEZMFCZK\\MRGVGfAYDAh@Mb@KvA]f@MREdAWt@ODAn@Qn@Oh@Md@KJCl@OLCXGJCTGr@Qt@UTIr@SBARIPILETIj@Yd@UPINIJGDE@?^Uj@a@PKLKHGROHINMLKNMNKTUXYBC@ATUFGPSTWnAwAVY\\_@hBuBBCxAcBbBmBrA{ArA}AHKPQFIX]PQFKV[Za@b@o@\\k@PYNYNUBINWRc@LWTg@Na@Tm@\\aAPe@H[FU@EHUNg@XgAVy@\\iAPk@FOFUNg@Lg@Lg@Ng@xAmFZmANg@@IFOb@}A\\mAV}@?ARu@^oALg@Ne@V_ALe@@ARu@~CaL^qAb@qAx@sB^{@R]Ra@Zg@LWjAgB@APWDGRWRU\\_@BC@C@A`@_@t@u@HGDEZYPMJIb@_@^]BCd@c@\\]NQJKJMX]RWJMLQNST]LSj@{@Vc@\\k@Te@P[\\w@Rc@Ri@Nc@Nc@Ne@FUj@wCHa@FYJi@DUDYL}@Da@D[Di@Fs@Fk@LeBFkAPaCLcBDm@HuAB_@D]Dg@Hm@DYBQHg@D[He@Lk@F[HYF[FU@CV_ALa@FSHU^cAVs@\\{@\\{@@CL[J[p@cBTk@Zy@b@gA@A`AeCJYl@{ADMd@kAFQPc@JYPc@JY@AJYRc@Xq@Vi@HOTc@Zq@Vc@Ta@d@y@Ta@nBgDNYh@}@v@qA^q@RYNWV]HMV[BCRWj@q@h@i@`A}@NMROVQRMJGZQ|@c@BAZOf@QhAc@r@W`@MrB{@LEp@Wp@WHEf@Sb@OXMXKXKVKRIFCNGVKTIXKVK`@ONGn@Ul@UZMVKVIZMTIVKVMVKJGHGVMVMTOVOVQTORO@?RQTQVSbAaAh@k@\\]HKHMJMHKx@mAFKz@yATc@P[R[\\u@^u@\\u@Xm@?ARc@HQh@kAn@wADIb@_AJWTe@BEZs@Rc@HQ\\s@Zs@LW?A\\u@LYFKFMZs@NYx@gBN[Zs@\\u@LW\\s@LWN]Ve@FKNW^o@PWNWRYNUPW@CV]Xa@PURYPURUPSPUTWPSRSPSTUFGJKRSRSRQRQVUh@e@POdAw@ROTQTOVQROv@g@@Af@[NK`Ao@VOTOZUNIl@a@DENKj@_@RMBCTOb@WHGRO@?TOVQVQRMFELINKFCTQBARORMVOTQTOTMVQTOVQxAaAd@[ZSTOVQBAZSBCFETOd@W`@YLIz@o@HGRO^[VS~@{@bB}ARSp@m@t@s@@AVWDCXY|@y@tCmCNMp@o@BCZYPQpAmATSf@g@^[|@{@|AyALKVWb@a@z@y@^]f@e@f@e@TSPO~A{At@s@n@m@`A_ATU`@a@bBaBPQZ[TWJIFGRSt@u@f@g@@Af@e@VWn@o@^_@b@c@PQb@c@l@k@\\]p@s@~@_A`B_BFEn@q@Z]XYZ]`@_@DGr@q@^a@PQ`@a@LM`@_@XY^_@XYhAiAJIJK^_@HIlAmAb@c@j@o@PWNM\\]JMPOTUJKRUTS@A@ATU\\]d@e@VWpAqA@?X[DETURS@ADC?AZY?Ad@c@b@c@RSPQd@e@RQDGLKVWFIHIZYDEXYRSBC`@a@XYLKFIj@i@LMTURU\\_@V[\\c@Va@T]LSZg@LUb@y@@Ab@w@N[JSLW^u@FKFMLWN[NWN[LWNWN[JQBGBGJSDIBCBINYLU@ANYLYLWPYLWNYNYPYNWNUPYNURWNSBENQDGLONQTUJMDGVUPQBELMVSPQTSTOVSRO@ATOTORMVQXMVOTMTKVMVMn@[TKTMp@[FEh@WTKPIDCRKLGJEXORKXMPKBAVMTMHENIVMVONIBCXOPMXQTOVQRQTQRQTQRSFGJKRSRSRURURSPSTURUZ_@JMPQRUPQRURSRUNQTWTURUPSPS@APQRUTUPSRUPSTUPSRURSRUBCr@q@VWTUTSRQTSb@]XUj@c@TONK^WXSVQDCd@[b@Y`@WVQVOROZQRMVQTMHGNKTORMVSROVSXUVSNOPOPORS@?RSRSLMFGPSRSRUFGJKDGNONQHIJKJMVYNQPQPSPSJKBCNQPSX[HGNQRUTUBE@APSRSRURURSRUPQ@A@ABCLMDELMXYd@a@PQTQ`@[r@c@HGJGTQVOPKdAs@VOVMJGJGTMVOVMJGJGTMTMVOVMTMVO^SrAu@`Ag@NK`@UXOl@]TM\\QTOl@_@l@a@r@g@LKn@g@LKx@q@r@o@NQRSZ[n@q@TWZ]d@g@LMPQHIJKJMPODGDCPQb@e@JOVW^a@VYXYNSx@{@HIp@s@JK|@aAp@u@HKRSRSHI^a@LOj@m@JMXYJMHIHK\\]RSVYPUFIRUHI@Ad@i@LMNOr@w@`@a@hAmALKX[b@e@LMZ_@f@i@f@g@BCTWFGRU`@e@b@c@VYTUTWVYJK`@c@\\_@NOl@q@bAgAVYb@e@LM`@a@FIX[FGr@w@fAiAVWPOTUVYJMDGJIHKf@m@X]^_@xA_Bl@o@\\_@h@k@FIzA_B@?DG\\_@BCLMBEFEHKRUTUHKBCPQBENODENOBEPSRQ@CTWRSRS@CTUPSVYJKJKTWX[RUHGZ]HINQTWz@}@NQTUt@y@JMBADGt@w@bAiA|@_Ar@w@j@m@h@m@j@k@t@w@`AaAhBqBlAoAxA}An@q@`@c@bAgAb@e@n@s@|AeBlAuAlAsArAyAj@k@X]j@m@?ADETW^a@bAiAr@y@~@eA|@aAfAoAd@g@f@m@FGV]FILQDEPWZg@@CLSBEXk@LYLWN_@HSJ[FSNe@Jc@J]Jg@@EHa@Hc@F_@Fg@JkAN_BDm@BYFm@B]BOPyBR}BPmB@MB]D]Dg@@SBWH}@De@Fi@@UDa@Da@B[B_@D_@B]?AD]B]D]Fw@NaBDc@B]B]BO@O@I@SH}@?AD[B_@D_@B[Dc@B_@BUBWDk@D_@B[BM@OFc@D]F_@?ADYF]F]F]F[H]DUBIF[H]H[J[HU@CL[L[HW@AJYL]L[L[JY@A`@gAh@oA\\cAJ[Zu@Xw@z@yBZ}@^_Ah@wATk@Z}@HQFQPe@HYL_@FSBIHYFYJ_@H_@F[FYFa@DS?EHe@Hw@BU@GB_@BSB]Bk@B_@?M@Q@YBc@?]?_@CyACoAAw@C}ACoACkA?M?O?GE{B?CCs@?a@A_@E_CA]A{@A{@Ai@ASAq@A_AA]ASA_@Ay@AaA?]?O?O@a@@]@q@Dm@B[B]D_@DY?GDYHc@Fa@DSHa@FUNo@ZcAHUHSJWHQ@EN[LYP]HSJSTYPWJMT]h@s@T[LORYFI^g@LQ|@oAn@y@p@}@LODGLSNUBCLWPYLWNYP[Ro@Na@J]\\_ABML_@H_@Ha@Hi@He@Hk@Fi@Fi@B_@Bi@@m@F}BBs@HyDFqCHyDDcBBmADcBDaBB}AH{C@g@@_@B_@B]B]Dg@DUD]D]F]Hc@DWH]H]H[J]J[HWN_@JYN]N]HMN]PYVc@Xc@NSPUTWPURSPQFGJKTQTSRQXSPQTQTSTQLKDEROTSh@c@POVSVUf@a@TQTSRQTQRSJKHGNOPQVWVYNOTWDGLOPQPUPWVYJORWPUPUDETWHMb@i@PURWRU?APSPUPUHIn@{@LOV[@AV]JMTYLQ`@g@RWPSLO^e@RWf@o@fAuA`@i@TWt@aAv@aAdAsAjAwA|AmBhAsA@An@q@^c@NSRUPSTSPSHG^]RSPM@ARQPQXSDELK|@s@z@m@LITOLKPK`@W`@WNIJGf@[FCDEHEVQh@YDEDCp@a@n@_@PKj@]VODCj@[HEnAw@zA}@xA}@|BuADELGRM\\SVOj@]~@i@n@]VOXOTOPKDA`B}@HEDCPKXOTKNIZQDAFEPKl@]HCn@a@r@g@|@s@ZW@AZ[XWRU\\_@RUTYNS@CBC^i@BE@A^k@l@cA?AfAcBBEDK@?HMJQn@eALSP[DEDIHOLS^o@BGHMFMHMXm@NYPc@^w@j@qAPc@JWVo@Zq@Tk@Ti@\\s@N[HOTe@P[JSRa@^q@Ta@PYFKLUFKHMZg@~@yALQNUHKt@aAZe@b@k@HMRWT[\\c@NSNSp@}@f@k@@AV[TYLQRYV]HKNS`@k@d@s@v@iA|@sAhA_B@?DILQ`@k@`@m@JMFM`@o@DEp@cANWb@o@^k@f@w@b@u@PWNWT_@Zi@PYNYP[JUJWNYLYPa@Tg@v@eBVm@r@}AJWN[HQLYHS^q@Tc@^k@Va@PWNSNSV_@Z_@RUFIJK\\]h@g@`@_@l@g@h@_@^Wz@k@LIt@e@x@i@XSVQROVSTSXY\\]POl@o@TUd@i@NQLO^a@^i@f@q@\\m@@AHMVa@`@s@\\q@^o@d@{@LW`@q@p@oADIVe@R_@@CBE@CNWp@kA\\q@NY`@q@FIJOPW@CLQNQDELQNQNQRSVU@APOTQXSNMTM@AVOXONILEJEh@SPGRGLEPE^KPEPEb@INC`AQBApAUJCVEp@MTEVGRCb@KRGTGXIZMPG`@QTMf@WBATOTORO@?VSVURQNOXYLODCPURWTY@A\\g@b@q@t@iA`@o@FIPWf@w@DI`@m@PYHMDGZe@b@q@PWNUR[bA{AJQn@aAR[FKRY`@o@h@w@JQJOPWR[Xe@Va@PYPWPWNUPW`@m@@AJSBCPYPWb@o@`@m@b@q@PWNUb@q@PW\\k@JOFINSR[NWXa@FKPURYNURWPUPQTYNQPONQr@o@RQh@e@VQTQTOVQPKXQJGh@Y@APIPKnB_ARK`@S`@SDCPINIfAi@p@]VKn@]l@Yn@[l@YRMZO\\Q`Ae@VMNI\\Qf@[FCVQRMVQPMVSTQTQTSNMDCRSTSNMDEPSTURURSZ_@Zc@RWJODE`@m@JQT]PYJQPY@EPY@CJUPYJWJSVk@HQJYL[L[J[L]J[HYL_@HYH]Pq@h@_CLg@DQ^{AHYH[J[J[J]LYl@yA@ALYHODINWJSBENUP[PUPWPWNQBCPSRUZ]JKRQTSPOfAu@TM@ARMXOTMXOTKZMl@Uf@Q`@M@?VGp@OLCZGb@IXGXExAYFAnAUnAUVG`@INCXETG\\Gr@Mj@K^GhAS\\EZGVC`AMjBUxASp@IVCv@KTCF?XE|@KJCRC`@Gp@MDAVGl@OPG`@Kp@Sr@Uj@OHC~@YVIDAXIRGFCTGXIFAJELCNETG^GJC`@IdAUREf@K\\GFA\\Gd@IVGn@MXEp@Mx@Ql@Mj@OnB]`B[ZIz@Ob@Kp@Md@IbASREd@Ir@MzAY@A\\Gh@KFAzCk@VGjAUr@MVGbB[NCb@Ij@Mn@KDA\\GXGVGr@MDA~@QZG^IrBa@nAUb@If@InAULELCZGrAW~A[|@Q`@IxAY@?r@OXITG\\ITGZITGDCVIXIZK\\Md@OVKFCf@QLEJE@ANGZMLGTKXMVKn@YHCTKZO\\OHE^O^QVK`@QrAk@BAZMZMHEFC\\MZMDANGPIRKj@U`@QNIh@Uj@Wd@Sh@UZOPI`@OVMLEPIPIb@Sn@Wj@WZMJEZORIJGTKLG@AVMLI^WPKDEROROTSRSTSJKBENQTYNQPUT[Xe@HMHKNWNUHMLSLSHOT_@T_@NWFKHMR[^q@@?R_@^m@HK\\k@FKp@kAJQZm@Tc@h@iABEJU`@y@JUh@kAfAaC\\}@Tk@N_@N]Vq@Xq@Ri@FOJUVo@JY\\}@HQ\\{@Rg@DMZs@h@qA`@gA`@cAPc@N]Rc@Xm@DIZo@NYb@u@FKLSXg@j@{@\\i@p@eAT_@pAsBV_@Va@d@w@LUNYHOJO\\i@\\i@p@eAh@y@Vc@T]NUZe@RYT[FIl@u@BCRURSJKX[VUTSDEJIXWv@k@|@k@x@g@vA{@nAu@^S`BaAFEFELIFGh@c@h@c@HEhBeBDEf@g@ZYh@i@`C_Cf@e@z@{@RQTU~@_Aj@i@VUtAuATS|@}@JKl@k@`AaAd@c@PQHIFGHIVU`@a@t@u@x@w@XWf@g@~@y@^_@PQRQJKRSPQRQFGZ[DE\\[TWPOJKLMNORSVY@AFEp@u@V[TWDG\\a@LQTY?APUPUPW`@m@HOb@q@T_@T_@NW?AHMNYLSBINYR_@"
                                    },
                                    "start_location":
                                    {
                                        "lat": 37.5909837,
                                        "lng": -121.3339934
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance":
                                    {
                                        "text": "0.9 mi",
                                        "value": 1422
                                    },
                                    "duration":
                                    {
                                        "text": "1 min",
                                        "value": 71
                                    },
                                    "end_location":
                                    {
                                        "lat": 34.0786054,
                                        "lng": -118.2284092
                                    },
                                    "html_instructions": "Take the <b>CA-110 S</b> exit toward <b>Los Angeles</b>",
                                    "maneuver": "ramp-right",
                                    "polyline":
                                    {
                                        "points": "oy`oEv}spUZG@?@ABEn@gAVc@DGJQLSLUr@mAl@cAr@mAR[NWNWNU`@m@@ArAqB\\g@v@iA`@m@FKlAiBRWVa@z@oAvAuBFIb@q@b@o@`@m@PUT[NQRQFINK@ARQBARKHENGBADAJEDAHCLAPEFAPABADALADARCDARED?DC@?JEB?@ADCFCDCJIBANKJGHELIFCDCHEHEJELGNILEJEJEJCHCNCREFALAB?B?@?B@B?@?B@B?B@@@D@D@DBB@BBB@@B@?@@@@@B@?BB@@@BBBBDDF@B@@NRLRPVRXPVJNBDBB@@@?R@"
                                    },
                                    "start_location":
                                    {
                                        "lat": 34.08807609999999,
                                        "lng": -118.2359573
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance":
                                    {
                                        "text": "1.4 mi",
                                        "value": 2298
                                    },
                                    "duration":
                                    {
                                        "text": "2 mins",
                                        "value": 135
                                    },
                                    "end_location":
                                    {
                                        "lat": 34.0647714,
                                        "lng": -118.2457519
                                    },
                                    "html_instructions": "Merge onto <b>CA-110</b>",
                                    "maneuver": "merge",
                                    "polyline":
                                    {
                                        "points": "i~~nEpnrpUz@rA`@l@Zb@JJLRHLJL^f@bAtA^d@NTt@`A`@d@v@|@FFHHLNRRNL@@RRVVPPPP?@HHXX`@^FFLNLLNNPN^^`@`@`@b@FFNLJLXXJJ^\\DDLLRRRP?@TTVTHFJJTPHFLHVPLF\\RVLVJd@RRFp@V`A\\`@Nb@NnAd@B?fA`@VJD@HBj@TTLNJHFl@ZLHVP^XB@LLRNRRb@d@PTPRV^JRDDNXJRXj@FNL\\DHN`@LXTh@JXL\\HPN\\Vr@JTN^Vp@FLFLJXN\\Tl@Rf@Rh@^z@t@lBFNJXLVr@hBFPL\\FTFRTbAFXDXHr@Hh@VrBNbAXnA"
                                    },
                                    "start_location":
                                    {
                                        "lat": 34.0786054,
                                        "lng": -118.2284092
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance":
                                    {
                                        "text": "449 ft",
                                        "value": 137
                                    },
                                    "duration":
                                    {
                                        "text": "1 min",
                                        "value": 8
                                    },
                                    "end_location":
                                    {
                                        "lat": 34.0643518,
                                        "lng": -118.2471139
                                    },
                                    "html_instructions": "Take the <b>US-101 Fwy</b> exit",
                                    "maneuver": "ramp-right",
                                    "polyline":
                                    {
                                        "points": "yg|nE|zupUEd@?B?@?@?@FZDTBNDLDNBLFRPb@\\x@"
                                    },
                                    "start_location":
                                    {
                                        "lat": 34.0647714,
                                        "lng": -118.2457519
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance":
                                    {
                                        "text": "0.5 mi",
                                        "value": 773
                                    },
                                    "duration":
                                    {
                                        "text": "1 min",
                                        "value": 44
                                    },
                                    "end_location":
                                    {
                                        "lat": 34.0591432,
                                        "lng": -118.2456346
                                    },
                                    "html_instructions": "Slight <b>left</b> onto the ramp to <b>I-10 E</b>/<wbr/><b>I-5 S</b>",
                                    "maneuver": "ramp-left",
                                    "polyline":
                                    {
                                        "points": "ee|nElcvpUHJ@@x@|Aj@bAJRJPBDFJDFLPNNTNRLRHTFJ@F@|@Fj@BT@H?VAN?FAD?JCHADCVIPKNMRQ\\[RQPOTUFGNBFGLOJMLKLOLOFEBCJOFGFGFIHGJMDGFGPSLSLQFMRa@Ra@Tk@LSFMHOLUNS@_@"
                                    },
                                    "start_location":
                                    {
                                        "lat": 34.0643518,
                                        "lng": -118.2471139
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance":
                                    {
                                        "text": "0.1 mi",
                                        "value": 217
                                    },
                                    "duration":
                                    {
                                        "text": "1 min",
                                        "value": 9
                                    },
                                    "end_location":
                                    {
                                        "lat": 34.0578287,
                                        "lng": -118.2438884
                                    },
                                    "html_instructions": "Merge onto <b>US-101 S</b>",
                                    "maneuver": "merge",
                                    "polyline":
                                    {
                                        "points": "sd{nEdzupUfA{An@{@b@o@x@mAn@eA"
                                    },
                                    "start_location":
                                    {
                                        "lat": 34.0591432,
                                        "lng": -118.2456346
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance":
                                    {
                                        "text": "0.1 mi",
                                        "value": 172
                                    },
                                    "duration":
                                    {
                                        "text": "1 min",
                                        "value": 19
                                    },
                                    "end_location":
                                    {
                                        "lat": 34.0567929,
                                        "lng": -118.2425932
                                    },
                                    "html_instructions": "Take exit <b>2C</b> for <b>Broadway</b>",
                                    "maneuver": "ramp-right",
                                    "polyline":
                                    {
                                        "points": "m|znEhoupU^?FIRUNU@CHMJSZk@NYXg@d@y@"
                                    },
                                    "start_location":
                                    {
                                        "lat": 34.0578287,
                                        "lng": -118.2438884
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance":
                                    {
                                        "text": "492 ft",
                                        "value": 150
                                    },
                                    "duration":
                                    {
                                        "text": "1 min",
                                        "value": 31
                                    },
                                    "end_location":
                                    {
                                        "lat": 34.0557277,
                                        "lng": -118.2435907
                                    },
                                    "html_instructions": "Turn <b>right</b> onto <b>N Broadway</b>",
                                    "maneuver": "turn-right",
                                    "polyline":
                                    {
                                        "points": "}uznEdgupUJJJJPNHHf@d@\\Zb@^t@r@"
                                    },
                                    "start_location":
                                    {
                                        "lat": 34.0567929,
                                        "lng": -118.2425932
                                    },
                                    "travel_mode": "DRIVING"
                                },
                                {
                                    "distance":
                                    {
                                        "text": "413 ft",
                                        "value": 126
                                    },
                                    "duration":
                                    {
                                        "text": "1 min",
                                        "value": 34
                                    },
                                    "end_location":
                                    {
                                        "lat": 34.0549009,
                                        "lng": -118.242651
                                    },
                                    "html_instructions": "Turn <b>left</b> onto <b>W Temple St</b>",
                                    "maneuver": "turn-left",
                                    "polyline":
                                    {
                                        "points": "ioznElmupUXY?ANQb@g@PS`@g@NQNQBE"
                                    },
                                    "start_location":
                                    {
                                        "lat": 34.0557277,
                                        "lng": -118.2435907
                                    },
                                    "travel_mode": "DRIVING"
                                }
                            ],
                            "traffic_speed_entry":
                            [],
                            "via_waypoint":
                            []
                        }
                    ],
                    "overview_polyline":
                    {
                        "points": "m|peFv_ejVtd@_CqAwp@pAe[eJkBk_@oC}|@guAuxCcdDwe@{v@oUs_Bg\\_sEaJoaBeC}r@jPcnAdOm_A|Ysi@df@uN|P{n@hu@yqBlQ_lAz]ys@xg@k~@xHgtAbz@ivB``A{{@pf@oNha@vV|h@iPfc@oc@tj@gW|y@_Qlu@y_@t\\yi@vsAaxBve@ot@kBcdB{Pw{Dah@o_A{Juu@pCo|@aLaaBl]mgDhFirAiEciCkTysEtA{eJfCcjJFcoBkMezBc@qlB_k@yiBgo@a`CqTodBrBq`AfO_v@in@axCir@m_Bgh@cwF_HuvAnQowAx~ByrCrrB{}DtxBahEv`IoqOvzDydGjuCebEh_I}vK`kFowGjbEktD`oC{~AbzBy}@dzAi~@ng@g[t~Awl@ruE_eA`mDcw@l}GohAzmFc|@bnBk[xuBqj@pjAip@nzByoAzhDymBjaCstAdqDgxCl_GswF|nHs`H~bEeyD~iDyoEb|BwfCjyDyfDvoI}fF~_JsqFddToiN|xDwmCdiA{w@|s@{|@dmD_fFprDulFj`F_iHn`FqdF`tL_pKfxMefLnvCqbCdcE{|Ct|JuoF~}Fm_DtnF_oE|zJczItgAusAxsAwkC|qB_bEpsBigEvxByrDxxGy_H~vHi~H~aDgcD`zGc`Gxc]ypUhaL_vHx}G_dGzeM{mN`wDiwFf~Se}[zjI_oMbhEycFjuIkkJvyOylQrkMmsNdnDolDzhAevAtiB{s@|kH_~A|lBa_@li@e@lo@iQtaA_Xbn@dApq@gMdl@wq@xMsf@rk@}m@~pBiyBjvCmiBnp@`c@rp@nr@zm@bk@na@e@rz@{_AbQo]vFi|@rKyaBhQi|@fnAmzBnv@agAxn@g]p}@aGzlBtMdpBdB~vBck@dhB_jA~c@_c@vQym@fuAegAfyAiZ`^cc@tUkpA|rAgyA~k@uWln@iDtzBkJjfAqpAxZww@jz@wq@dvA_gCbl@my@|~@sa@x{Aky@h_Biq@dpAm{@|y@sIxy@jJl~@sCt|@wZlxAkcC|eA_p@dfAe`@j{Cst@rsCwtAbw@om@jj@o~A`U}Z`Hul@tm@enAnx@af@le@{{@rzBikBhqAs}AzoAsbA~vAmkAt_BgeBpt@gx@lJk]|JaaApT{iAI{f@nQy]vS}zA|d@af@fnBaeBp`BabC|xA_{Adq@qm@pc@gq@fQoTze@kJfdAsStxBms@|h@mgA`eAahArtA{~AhN`A|g@ph@bYxQ`Phb@pJz\\xOqBtL_RhJ{LlJ?"
                    },
                    "summary": "I-5 S",
                    "warnings":
                    [],
                    "waypoint_order":
                    []
                }
            ],
            "status": "OK"
        }
        fuel_stops = calculate_fuel_stops(route)

        # Verify that fuel stops are calculated correctly
        self.assertIsNotNone(fuel_stops)
        self.assertGreater(len(fuel_stops), 0)

class RouteFuelStopsAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        FuelPrice.objects.create(
            opis_truckstop_id=1,
            truckstop_name="Shell Gas Station",
            address="123 Broadway Ave",
            city="New York",
            state="NY",
            rack_id=101,
            retail_price=3.899999
        )
        FuelPrice.objects.create(
            opis_truckstop_id=2,
            truckstop_name="Chevron Gas Station",
            address="456 Sunset Blvd",
            city="Los Angeles",
            state="CA",
            rack_id=102,
            retail_price=4.250000
        )

    @patch("calculator.utils.calculate_fuel_stops")
    def test_route_fuel_stops_success(self, mock_calculate_fuel_stops):
        mock_calculate_fuel_stops.return_value = [
            {"city": "New York", "station": "Shell Gas Station", "price": 3.899999},
            {"city": "Los Angeles", "station": "Chevron Gas Station", "price": 4.250000}
        ]

        response = self.client.post(
            "/api/route-fuel-stops/",
            data={"start_address": "New York, NY", "finish_address": "Los Angeles, CA"},
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0]["city"], "New York")

    def test_route_fuel_stops_failure(self):
        response = self.client.post(
            "/api/route-fuel-stops/",
            data={},
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
