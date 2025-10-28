# UP is down and down is UP

## Misc

### Here's the flag, but the alphabet characters are completely UPside Down.  Fix it and you'll get the flag.
### TERACTF{i_HOpe_yOuR_Not_gOINg_To_AttEMPT_thiS_bY_hAnd_bEcAuSe_tHErE_iS_n0_pATTerN_ANd_dOIng_iT_by_hANd_c0ULD_leAD_tO_TypOs_WHicH_wIlL_lEAd_To_TrOubLe_TiCkeTs_OR_wORse_iT_cOuld_LEad_to_ENNui_anD_ThAt_CaN_lEad_TO_twIDDliNg_yOur_ThumbS_And_THat_WilL_ONly_LEAD_To_MOre_ennUI_aNd_WhO_waNts_ThaT?}
### P.S. You'll probably want to make a short script or use a command line.  
### P.P.S AI won't make you smarter

Well that's a lot of flag...this is pretty easy from a UNIX terminal.  I have no idea how to solve this in Windows (without WSL).

The clue is indicating the uppercase letters should be lowercase, and vice versa.  

For me the easiest way to do this was to use the [tr](https://man7.org/linux/man-pages/man1/tr.1.html) command in UNIX.

```sh
% echo "TERACTF{i_HOpe_yOuR_Not_gOINg_To_AttEMPT_thiS_bY_hAnd_bEcAuSe_tHErE_iS_n0_pATTerN_ANd_dOIng_iT_by_hANd_c0ULD_leAD_tO_TypOs_WHicH_wIlL_lEAd_To_TrOubLe_TiCkeTs_OR_wORse_iT_cOuld_LEad_to_ENNui_anD_ThAt_CaN_lEad_TO_twIDDliNg_yOur_ThumbS_And_THat_WilL_ONly_LEAD_To_MOre_ennUI_aNd_WhO_waNts_ThaT?}" |tr '[:upper:][:lower:]' '[:lower:][:upper:]'
```
This reversed case for all the letters and gave the flag.

**teractf{I_hoPE_YoUr_nOT_GoinG_tO_aTTempt_THIs_By_HaND_BeCaUsE_TheRe_Is_N0_PattERn_anD_DoiNG_It_BY_HanD_C0uld_LEad_To_tYPoS_whICh_WiLl_LeaD_tO_tRoUBlE_tIcKEtS_or_WorSE_It_CoULD_leAD_TO_ennUI_ANd_tHaT_cAn_LeAD_to_TWiddLInG_YoUR_tHUMBs_aND_thAT_wILl_onLY_lead_tO_moRE_ENNui_AnD_wHo_WAnTS_tHAt?}**


