# Code listing

# main_main

```c
// main.main
void __fastcall main_main()
{
  __int128 v0; // xmm15
  uint8 *str; // rcx
  unsigned __int64 v2; // rax
  _slice_interface_ v; // [rsp+0h] [rbp-18h] BYREF
  string v4; // 0:rax.8,8:rbx.8
  _slice_interface_ v5; // 0:rax.8,8:rbx.8,16:rcx.8
  _slice_interface_ v6; // 0:rax.8,8:rbx.8,16:rcx.8

  if ( os_Args.len < 2 )
  {
    v.array = (interface_ *)&RTYPE_string_0;
    v.len = (int)&main__stmp_1;
    v5.array = (interface_ *)&v;
    v5.len = 1LL;
    v5.cap = 1LL;
    log_Fatal(v5);
  }
  if ( os_Args.len <= 1uLL )
    runtime_panicIndex();
  str = os_Args.array[1].str;
  main__addr.len = os_Args.array[1].len;
  if ( *(_DWORD *)&runtime_writeBarrier.enabled )
    runtime_gcWriteBarrierCX();
  else
    main__addr.str = str;
  github_com_hajimehoshi_ebiten_v2_SetWindowSize(main_ScreenWidth, main_ScreenHeight);
  v4.str = (uint8 *)&title;
  v4.len = 16LL;
  github_com_hajimehoshi_ebiten_v2_SetWindowTitle(v4);
  v4.str = (uint8 *)&go_itab__ptr_main_Game_comma_github_com_hajimehoshi_ebiten_v2_Game;
  v4.len = (int)&runtime_zerobase;
  v2 = (unsigned __int64)github_com_hajimehoshi_ebiten_v2_RunGame((github_com_hajimehoshi_ebiten_v2_Game)v4);
  if ( v2 )
  {
    *(_OWORD *)&v.array = v0;
    v.array = *(interface_ **)(v2 + 8);
    v.len = (int)&runtime_zerobase;
    v6.array = (interface_ *)&v;
    v6.len = 1LL;
    v6.cap = 1LL;
    log_Fatal(v6);
  }
}
```

## main.(*Game).Draw

```c
// main.(*Game).Draw
void __golang main__ptr_Game_Draw(_ptr_main_Game a1, _ptr_ebiten_Image a2)
{
  golang_org_x_image_font_Face font; // rdi
  string str_connecting; // 0:rbx.8,8:rcx.8

  if ( main__state > 1 )
  {
    if ( main__state == 2 )
    {
      main__ptr_Game_D_Pathfind(a1, a2);
    }
    else if ( main__state == 3 )
    {
      main__ptr_Game_D_END(a1, a2);
    }
  }
  else if ( main__state )
  {
    if ( main__state == 1 )
    {
      font = main_mplusBigFont;
      str_connecting.str = (uint8 *)&::str_connecting;
      str_connecting.len = 14LL;
      github_com_hajimehoshi_ebiten_v2_text_Draw(
        (github_com_hajimehoshi_ebiten_v2_Image *)a2,
        str_connecting,
        font,
        475LL,
        300LL,
        main__c_yellow);
    }
  }
  else
  {
    main__ptr_Game_D_Main_menu(a1, a2);
  }
}
```

## main.(*Game).Update

```c
// main.(*Game).Update
error_0 __golang main__ptr_Game_Update(_ptr_main_Game a1)
{
  void *tab; // rax
  void *data; // rbx
  error_0 v3; // kr00_16
  error_0 v4; // kr10_16
  error_0 v5; // kr20_16
  error_0 v6; // kr30_16
  error_0 result; // 0:rax.8,8:rbx.8

  if ( main__state )
  {
    if ( main__state == 1 )
    {
      v5 = main__ptr_Game_U_Connecting(a1);
      data = v5.data;
      tab = v5.tab;
    }
    else if ( main__state == 2 )
    {
      v3 = main__ptr_Game_U_Pathfind(a1);
      data = v3.data;
      tab = v3.tab;
    }
    else
    {
      v4 = main__ptr_Game_U_END(a1);
      data = v4.data;
      tab = v4.tab;
    }
  }
  else
  {
    v6 = main__ptr_Game_U_Main_menu(a1);
    data = v6.data;
    tab = v6.tab;
  }
  result.data = data;
  result.tab = tab;
  return result;
}
```

## main.(*Game).U_Main_menu

```c
// main.(*Game).U_Main_menu
error_0 __golang main__ptr_Game_U_Main_menu(_ptr_main_Game a1)
{
  __int128 v1; // xmm15
  retval_5E9DA0 v2; // kr00_16
  string v3; // kr10_16
  runtime_itab *v4; // rax
  void *v5; // rax
  void *v6; // rbx
  _slice_interface_ v; // [rsp+10h] [rbp-18h] BYREF
  string v8; // 0:rdi.16
  error_0 result; // 0:rax.8,8:rbx.8
  _slice_interface_ v10; // 0:rax.8,8:rbx.8,16:rcx.8

  v2 = github_com_hajimehoshi_ebiten_v2_CursorPosition();
  if ( !main_connectionState )
  {
    v8.str = (uint8 *)":4444:path<nil>AdlamAllocAprilBamumBatakBuhidClassCommaDograEnterEqualErrorFLOATGlyphGreekIDENTKhm"
                      "erKind(LatinLimbuLocalMarchMatchMinusNRGBANushuOghamOriyaOsagePauseQuoteRANDRRangeRealmRunicSHA-1S"
                      "TermShiftSlashSpaceStdHWStdVWSubrsTakriTamilTypeAValueX: %dXGB: Y: %d\\n\\n+\\u202] = (abortarrayb"
                      "reakclassclearcloseconstdeferfalsefaultfilesfixedfloatfvec2fvec3fvec4gcinggscanhchanhflexhostshste"
                      "mhttpshvec2hvec3hvec4imap2imap3imapsinit inputint16int32int64linuxlstatmatchmheapmkdirmonthpanicpa"
                      "rsepop3srangerune scalescav schedshortsleepslicesse41sse42ssse3sudogsweeptext/tracetrap:uint8union"
                      "usingutf-8valuevstemwrite (nil) B ->  Value addr= alloc base  code= ctxt: curg= free  goid  jobs= "
                      "list= m->p= max=  min=  next= p->m= prev= span=% util%s %s;%s%s%s%s(%s)%s: %s%s[%d](...)\n"
                      ", i = , not , val .local.onion390625<-chanAccessAnswerArabicAugustBrahmiCANCELCarianChakmaCommonCo"
                      "pticCursorDeleteDigit0Digit1Digit2Digit3Digit4Digit5Digit6Digit7Digit8Digit9E: %v\n"
                      "EscapeExpectFormatFridayGOAWAYGOROOTGothicGray16HangulHatranHebrewHyphenInsertKOI8-RKOI8-UKaithiKh"
                      "ojkiLengthLepchaLycianLydianMondayNoticePADDEDPageUpPeriodPictOpPixmapPragmaRENDERRGBA64RejangSCHE"
                      "D STREETSTRINGStringSundaySyriacTai_LeTangutTeluguThaanaTypeMXTypeNSUgandaWanchoWeightWindowYezidi"
                      "[0][0][]byte\\ufffd\n"
                      "    \tacceptactionactiveallow";
    v8.len = 5LL;
    v3 = runtime_concatstring2(0LL, main__addr, v8);
    v4 = test_client__ptr_Con_Init(&main__con, v3);
    main_connectionState = 1;
    if ( v4 )
    {
      *(_OWORD *)&v.array = v1;
      v.array = (interface_ *)v4->_type;
      v.len = (int)v3.str;
      v10.array = (interface_ *)&v;
      v10.len = 1LL;
      v10.cap = 1LL;
      log_Fatal(v10);
    }
  }
  if ( github_com_hajimehoshi_ebiten_v2_internal_ui__ptr_Input_IsMouseButtonPressed(
         (github_com_hajimehoshi_ebiten_v2_internal_ui_Input *)&github_com_hajimehoshi_ebiten_v2_internal_ui_theUI->input,
         0LL)._r0
    && v2.x > 900
    && (unsigned __int64)(v2.y - 171) < 0x3B
    && v2.x < 1100 )
  {
    main__state = 1LL;
  }
  v5 = 0LL;
  v6 = 0LL;
  result.data = v6;
  result.tab = v5;
  return result;
}
```

## main.(*Game).U_Connecting

```c
// main.(*Game).U_Connecting
// local variable allocation has failed, the output may be wrong!
error_0 __golang main__ptr_Game_U_Connecting(_ptr_main_Game a1)
{
  string v1; // kr10_16
  string v2; // kr20_16
  unsigned __int64 Seed; // rax
  runtime_hmap *v4; // rbx
  __int64 v5; // rbp
  void *v6; // rax
  void *v7; // rbx
  runtime_hmap **v8; // rax
  uint64 *v9; // rax
  runtime_hmap *v10; // rdx
  int count; // rdx
  string *v12; // rax
  runtime_hmap *v13; // rbx
  __int64 v14; // r8
  __int64 v15; // rdx
  int v16; // rbx
  string *array; // rax OVERLAPPED
  int v18; // rcx
  __int64 v19; // rcx
  __int64 *v20; // [rsp+0h] [rbp-158h]
  _BYTE v21[64]; // [rsp+10h] [rbp-148h] BYREF
  uint64 key; // [rsp+50h] [rbp-108h]
  __int64 v23; // [rsp+58h] [rbp-100h]
  uint64 v24; // [rsp+60h] [rbp-F8h]
  int v25; // [rsp+68h] [rbp-F0h]
  runtime_hmap *h; // [rsp+70h] [rbp-E8h]
  __int64 v27; // [rsp+78h] [rbp-E0h]
  _slice_interface_ v; // [rsp+80h] [rbp-D8h] BYREF
  runtime_hiter it; // [rsp+F0h] [rbp-68h] BYREF
  __int64 v30; // [rsp+150h] [rbp-8h] BYREF
  string v31; // 0:rdi.16
  string v32; // 0:rdi.16
  string v33; // 0:rdi.16
  error_0 result; // 0:rax.8,8:rbx.8
  string v35; // 0:rbx.8,8:rcx.8
  _slice_interface_ v36; // 0:rax.8,8:rbx.8,16:rcx.8

  if ( !main__tcp.len )
  {
    v31.str = (uint8 *)":4444:path<nil>AdlamAllocAprilBamumBatakBuhidClassCommaDograEnterEqualErrorFLOATGlyphGreekIDENTKh"
                       "merKind(LatinLimbuLocalMarchMatchMinusNRGBANushuOghamOriyaOsagePauseQuoteRANDRRangeRealmRunicSHA-"
                       "1STermShiftSlashSpaceStdHWStdVWSubrsTakriTamilTypeAValueX: %dXGB: Y: %d\\n\\n+\\u202] = (abortarr"
                       "aybreakclassclearcloseconstdeferfalsefaultfilesfixedfloatfvec2fvec3fvec4gcinggscanhchanhflexhosts"
                       "hstemhttpshvec2hvec3hvec4imap2imap3imapsinit inputint16int32int64linuxlstatmatchmheapmkdirmonthpa"
                       "nicparsepop3srangerune scalescav schedshortsleepslicesse41sse42ssse3sudogsweeptext/tracetrap:uint"
                       "8unionusingutf-8valuevstemwrite (nil) B ->  Value addr= alloc base  code= ctxt: curg= free  goid "
                       " jobs= list= m->p= max=  min=  next= p->m= prev= span=% util%s %s;%s%s%s%s(%s)%s: %s%s[%d](...)\n"
                       ", i = , not , val .local.onion390625<-chanAccessAnswerArabicAugustBrahmiCANCELCarianChakmaCommonC"
                       "opticCursorDeleteDigit0Digit1Digit2Digit3Digit4Digit5Digit6Digit7Digit8Digit9E: %v\n"
                       "EscapeExpectFormatFridayGOAWAYGOROOTGothicGray16HangulHatranHebrewHyphenInsertKOI8-RKOI8-UKaithiK"
                       "hojkiLengthLepchaLycianLydianMondayNoticePADDEDPageUpPeriodPictOpPixmapPragmaRENDERRGBA64RejangSC"
                       "HED STREETSTRINGStringSundaySyriacTai_LeTangutTeluguThaanaTypeMXTypeNSUgandaWanchoWeightWindowYez"
                       "idi[0][0][]byte\\ufffd\n"
                       "    \tacceptactionactiveallow";
    v31.len = 5LL;
    v35 = runtime_concatstring2(0LL, main__addr, v31);
    if ( test_client__ptr_Con_Init(&main__con, v35) )
      main__state = 0LL;
    v32.str = (uint8 *)":4444:path<nil>AdlamAllocAprilBamumBatakBuhidClassCommaDograEnterEqualErrorFLOATGlyphGreekIDENTKh"
                       "merKind(LatinLimbuLocalMarchMatchMinusNRGBANushuOghamOriyaOsagePauseQuoteRANDRRangeRealmRunicSHA-"
                       "1STermShiftSlashSpaceStdHWStdVWSubrsTakriTamilTypeAValueX: %dXGB: Y: %d\\n\\n+\\u202] = (abortarr"
                       "aybreakclassclearcloseconstdeferfalsefaultfilesfixedfloatfvec2fvec3fvec4gcinggscanhchanhflexhosts"
                       "hstemhttpshvec2hvec3hvec4imap2imap3imapsinit inputint16int32int64linuxlstatmatchmheapmkdirmonthpa"
                       "nicparsepop3srangerune scalescav schedshortsleepslicesse41sse42ssse3sudogsweeptext/tracetrap:uint"
                       "8unionusingutf-8valuevstemwrite (nil) B ->  Value addr= alloc base  code= ctxt: curg= free  goid "
                       " jobs= list= m->p= max=  min=  next= p->m= prev= span=% util%s %s;%s%s%s%s(%s)%s: %s%s[%d](...)\n"
                       ", i = , not , val .local.onion390625<-chanAccessAnswerArabicAugustBrahmiCANCELCarianChakmaCommonC"
                       "opticCursorDeleteDigit0Digit1Digit2Digit3Digit4Digit5Digit6Digit7Digit8Digit9E: %v\n"
                       "EscapeExpectFormatFridayGOAWAYGOROOTGothicGray16HangulHatranHebrewHyphenInsertKOI8-RKOI8-UKaithiK"
                       "hojkiLengthLepchaLycianLydianMondayNoticePADDEDPageUpPeriodPictOpPixmapPragmaRENDERRGBA64RejangSC"
                       "HED STREETSTRINGStringSundaySyriacTai_LeTangutTeluguThaanaTypeMXTypeNSUgandaWanchoWeightWindowYez"
                       "idi[0][0][]byte\\ufffd\n"
                       "    \tacceptactionactiveallow";
    v32.len = 5LL;
    v1 = runtime_concatstring2(0LL, main__addr, v32);
    main__tcp.len = v1.len;
    if ( *(_DWORD *)&runtime_writeBarrier.enabled )
      runtime_gcWriteBarrier();
    else
      main__tcp.str = v1.str;
    v33.str = (uint8 *)&byte_6CB1DA;
    v33.len = 5LL;
    v2 = runtime_concatstring2(0LL, main__addr, v33);
    main__udp.len = v2.len;
    if ( *(_DWORD *)&runtime_writeBarrier.enabled )
      runtime_gcWriteBarrier();
    else
      main__udp.str = v2.str;
    test_client__ptr_Con_Register(&main__con);
    test_client__ptr_Con_JoinRoom(&main__con);
  }
  if ( (unsigned __int8)test_client__ptr_Con_ReciveStart(&main__con) )
  {
    Seed = test_client__ptr_Con_GetSeed(&main__con);
    test_game__ptr_Pathfind_Init(
      &main__gme,
      (test_game_Graph *)15000,
      Seed,
      (map_int_map_int_int *)10,
      test_images_Cities_txt);
    main__state = 2LL;
    v.array = (interface_ *)&RTYPE_string_0;
    v.len = (int)&main__stmp_0;
    v36.array = (interface_ *)&v;
    v36.len = 1LL;
    v36.cap = 1LL;
    log_Print(v36);
    if ( main__gme.path.len <= (unsigned __int64)(main__gme.path.len - 1) )
      runtime_panicIndex();
    key = main__gme.path.array[main__gme.path.len - 1];
    h = runtime_makemap_small();
    v4 = *(runtime_hmap **)runtime_mapaccess1_fast64(
                             (runtime_maptype *)&RTYPE_map_int_map_int_int_0,
                             (runtime_hmap *)main__gme.graph.matrix.arr,
                             key);
    v20 = &v30;
    ((void (__fastcall *)(_BYTE *))loc_47352B)(&v21[192]);
    v5 = (__int64)v20;
    runtime_mapiterinit((runtime_maptype *)&RTYPE_map_int_int_0, v4, &it);
    while ( it.key )
    {
      v24 = *(_QWORD *)it.key;
      v8 = (runtime_hmap **)runtime_mapaccess1_fast64(
                              (runtime_maptype *)&RTYPE_map_int_map_int_int_0,
                              (runtime_hmap *)main__gme.graph.matrix.arr,
                              key);
      if ( *(_QWORD *)runtime_mapaccess1_fast64((runtime_maptype *)&RTYPE_map_int_int_0, *v8, v24) == 1LL )
      {
        if ( main__gme.graph.names.len <= v24 )
          runtime_panicIndex();
        v9 = (uint64 *)runtime_mapassign_faststr(
                         (runtime_maptype *)&RTYPE_map_string_int_0,
                         h,
                         main__gme.graph.names.array[v24]);
        *v9 = v24;
      }
      runtime_mapiternext(&it);
    }
    if ( *(_DWORD *)&runtime_writeBarrier.enabled )
    {
      runtime_gcWriteBarrierDX();
    }
    else
    {
      v10 = h;
      main__moves = (map_string_int)h;
    }
    if ( v10 )
      count = v10->count;
    else
      count = 0LL;
    v25 = count;
    v12 = (string *)runtime_makeslice((runtime__type *)&RTYPE_string_0, 0LL, count);
    main__kiss.len = 0LL;
    main__kiss.cap = v25;
    if ( *(_DWORD *)&runtime_writeBarrier.enabled )
      runtime_gcWriteBarrier();
    else
      main__kiss.array = v12;
    v13 = (runtime_hmap *)main__moves;
    v20 = (__int64 *)v5;
    ((void (__fastcall *)(_BYTE *))loc_47352B)(&v21[96]);
    runtime_mapiterinit((runtime_maptype *)&RTYPE_map_string_int_0, v13, (runtime_hiter *)&v.cap);
    while ( v.cap )
    {
      v14 = *(_QWORD *)v.cap;
      v15 = *(_QWORD *)(v.cap + 8);
      v16 = main__kiss.len + 1;
      array = main__kiss.array;
      if ( main__kiss.cap < (unsigned __int64)(main__kiss.len + 1) )
      {
        v23 = *(_QWORD *)(v.cap + 8);
        v27 = v14;
        *(runtime_slice *)&array = runtime_growslice(
                                     main__kiss.array,
                                     v16,
                                     main__kiss.cap,
                                     1LL,
                                     (runtime__type *)&RTYPE_string_0);
        main__kiss.cap = v18;
        if ( *(_DWORD *)&runtime_writeBarrier.enabled )
          runtime_gcWriteBarrier();
        else
          main__kiss.array = array;
        v15 = v23;
        v14 = v27;
      }
      main__kiss.len = v16;
      v19 = v16 - 1;
      array[v19].len = v15;
      if ( *(_DWORD *)&runtime_writeBarrier.enabled )
        runtime_gcWriteBarrierR8();
      else
        array[v19].str = (uint8 *)v14;
      runtime_mapiternext((runtime_hiter *)&v.cap);
    }
  }
  v6 = 0LL;
  v7 = 0LL;
  result.data = v7;
  result.tab = v6;
  return result;
}
```

## test/game.(*Pathfind).Init

```c
// test/game.(*Pathfind).Init
void __golang test_game__ptr_Pathfind_Init(
        test_game_Pathfind *main_game,
        test_game_Graph *graph_size,
        int seed,
        map_int_map_int_int *number,
        string name_cities)
{
  __int128 v5; // xmm15
  map_int_map_int_int *v6; // rdx
  int *v7; // rax
  test_game_Pathfind *v8; // rdi
  test_game_Pathfind *v9; // rcx
  test_game_Pathfind *v10; // rdx
  test_game_Pathfind *pa; // [rsp+18h] [rbp+8h]
  runtime_slice v12; // 0:rax.8,8:rbx.8,16:rcx.8

  main_game->size = (int)graph_size;
  main_game->playerpos = 0LL;
  main_game->PrString.len = 0LL;
  if ( *(_DWORD *)&runtime_writeBarrier.enabled )
  {
    runtime_gcWriteBarrierR9();
    number = v6;
  }
  else
  {
    main_game->PrString.str = 0LL;
  }
  pa = main_game;
  test_game__ptr_Graph_Init(&main_game->graph, (int)graph_size, seed, number, name_cities);
  v7 = (int *)runtime_makeslice((runtime__type *)&RTYPE_int_0, 0LL, 0LL);
  v8 = pa;
  *(_OWORD *)&pa->path.len = v5;
  if ( *(_DWORD *)&runtime_writeBarrier.enabled )
  {
    runtime_gcWriteBarrier();
    v8 = v9;
  }
  else
  {
    pa->path.array = v7;
  }
  v12 = runtime_growslice(v8->path.array, 1LL, 0LL, 1LL, (runtime__type *)&RTYPE_int_0);
  v10 = pa;
  pa->path.cap = v12.cap;
  if ( *(_DWORD *)&runtime_writeBarrier.enabled )
    runtime_gcWriteBarrier();
  else
    pa->path.array = (int *)v12.array;
  v10->path.len = 1LL;
  *(_QWORD *)v12.array = 0LL;
}
```

## test/game.(*Graph).Init

```c
// test/game.(*Graph).Init
void __golang test_game__ptr_Graph_Init(
        test_game_Graph *graph,
        int graph_size,
        int seed,
        map_int_map_int_int *matrix_map_int_map_int_int,
        string names_cities)
{
  hash<int_comma_map_int_int> *p_runtime_hmap; // rax
  string v6; // r9
  int v7; // r11
  test_game_Graph *graph1; // rcx
  test_game_Graph *v9; // rdx
  int i_graph_size; // rax
  map_int_map_int_int *v11; // rax
  string *names; // rax
  int capacity; // rcx
  signed __int64 k; // rax
  int **v15; // rax
  int v16; // rdx
  runtime_hmap **v17; // rax
  runtime_hmap *v18; // rbx
  int v19; // rax
  int v20; // rdx
  runtime_hmap **v21; // rax
  _BOOL8 r1; // rbx
  uint64 v23; // rax
  int m; // rcx
  runtime_hmap **v25; // rcx
  int v26; // rdx
  int pointb; // [rsp+0h] [rbp-38h]
  int point; // [rsp+0h] [rbp-38h]
  int pointa; // [rsp+0h] [rbp-38h]
  int j; // [rsp+8h] [rbp-30h]
  uint64 key; // [rsp+10h] [rbp-28h]
  int i; // [rsp+18h] [rbp-20h]
  int seedb; // [rsp+20h] [rbp-18h]
  runtime_hmap *p_runtime_hmap_for; // [rsp+28h] [rbp-10h]
  map_int_map_int_int *numbera; // [rsp+58h] [rbp+20h]
  int names_cities_len; // [rsp+68h] [rbp+30h]
  string names_cities_copy; // 0:rax.8,8:rbx.8

  numbera = matrix_map_int_map_int_int;
  names_cities_len = names_cities.len;
  graph->matrix.sizex = graph_size;
  graph->matrix.sizey = graph_size;
  p_runtime_hmap = (hash<int_comma_map_int_int> *)runtime_makemap_small();
  if ( *(_DWORD *)&runtime_writeBarrier.enabled )
  {
    matrix_map_int_map_int_int = &graph->matrix.map;
    runtime_gcWriteBarrier();
    graph1 = v9;
  }
  else
  {
    graph1 = graph;
    graph->matrix.map = p_runtime_hmap;
  }
  i_graph_size = 0LL;
  while ( graph_size > i_graph_size )
  {
    key = i_graph_size;
    p_runtime_hmap_for = runtime_makemap_small();
    v11 = (map_int_map_int_int *)runtime_mapassign_fast64(
                                   (runtime_maptype *)&RTYPE_map_int_map_int_int_0,
                                   (runtime_hmap *)graph->matrix.map,
                                   key);
    if ( *(_DWORD *)&runtime_writeBarrier.enabled )
    {
      matrix_map_int_map_int_int = v11;
      runtime_gcWriteBarrierCX();
    }
    else
    {
      *v11 = (map_int_map_int_int)p_runtime_hmap_for;
    }
    i_graph_size = key + 1;
    graph1 = graph;
  }
  names_cities_copy.str = names_cities.str;
  names_cities_copy.len = names_cities_len;
  names = test_game_get_names(
            names_cities_copy,
            (__int64)graph1,
            (__int64)matrix_map_int_map_int_int,
            (__int64)names_cities.str,
            names_cities.len,
            v6,
            v7);
  graph->names.len = names_cities_len;
  graph->names.cap = capacity;
  if ( *(_DWORD *)&runtime_writeBarrier.enabled )
    runtime_gcWriteBarrier();
  else
    graph->names.array = names;
  math_rand__ptr_Rand_Seed(math_rand_globalRand, seed);
  for ( k = 0LL; graph_size > k; k = i + 1 )
  {
    i = k;
    v15 = (int **)runtime_mapaccess1_fast64(
                    (runtime_maptype *)&RTYPE_map_int_map_int_int_0,
                    (runtime_hmap *)graph->matrix.map,
                    k);
    if ( *v15 )
      v16 = **v15;
    else
      v16 = 0LL;
    while ( (__int64)numbera > v16 )
    {
      j = v16;
      v19 = math_rand_Int();
      if ( graph_size == -1 )
        v20 = 0LL;
      else
        v20 = v19 % graph_size;
      point = v20;
      v21 = (runtime_hmap **)runtime_mapaccess1_fast64(
                               (runtime_maptype *)&RTYPE_map_int_map_int_int_0,
                               (runtime_hmap *)graph->matrix.map,
                               i);
      r1 = runtime_mapaccess2_fast64((runtime_maptype *)&RTYPE_map_int_int_0, *v21, point)._r1;
      v23 = i;
      for ( m = point; r1 || m == v23; m = pointa )
      {
        seedb = math_rand_Int();
        v25 = (runtime_hmap **)runtime_mapaccess1_fast64(
                                 (runtime_maptype *)&RTYPE_map_int_map_int_int_0,
                                 (runtime_hmap *)graph->matrix.map,
                                 i);
        if ( graph_size == -1 )
          v26 = 0LL;
        else
          v26 = seedb % graph_size;
        pointa = v26;
        r1 = runtime_mapaccess2_fast64((runtime_maptype *)&RTYPE_map_int_int_0, *v25, v26)._r1;
        v23 = i;
      }
      pointb = m;
      v17 = (runtime_hmap **)runtime_mapaccess1_fast64(
                               (runtime_maptype *)&RTYPE_map_int_map_int_int_0,
                               (runtime_hmap *)graph->matrix.map,
                               v23);
      *(_QWORD *)runtime_mapassign_fast64((runtime_maptype *)&RTYPE_map_int_int_0, *v17, pointb) = 1LL;
      v18 = *(runtime_hmap **)runtime_mapaccess1_fast64(
                                (runtime_maptype *)&RTYPE_map_int_map_int_int_0,
                                (runtime_hmap *)graph->matrix.map,
                                pointb);
      *(_QWORD *)runtime_mapassign_fast64((runtime_maptype *)&RTYPE_map_int_int_0, v18, i) = -1LL;
      v16 = j + 1;
    }
  }
  test_game__ptr_Graph_Optimize(graph);
}
```

## test/game.get_names

```c
// test/game.get_names
// local variable allocation has failed, the output may be wrong!
string *__golang test_game_get_names(string names, __int64 a2, __int64 a3, __int64 a4, __int64 a5, string a6, int a7)
{
  runtime__type **p_bucket; // rcx
  __int64 v8; // rdi
  string *v9; // rax
  unsigned __int64 v10; // rcx
  int v11; // rbx
  string *array; // rax OVERLAPPED
  int v13; // rcx
  __int64 v14; // rdx
  _QWORD v16[2]; // [rsp+0h] [rbp-30h] BYREF
  _slice_string ret; // [rsp+10h] [rbp-20h] BYREF
  string v18; // 0:rsi.16

  p_bucket = &stru_7FC508.bucket;
  v8 = 1LL;
  v18.str = 0LL;
  v18.len = -1LL;
  strings_genSplit((int)names.str, *(_slice_string *)&names.len, v18, a6, a7);
  if ( v10 < 0x3A97 )
    runtime_panicSliceAcap();
  ret.array = v9;
  ret.len = 14999LL;
  ret.cap = v10;
  v16[0] = test_game_get_names_func1;
  v16[1] = &ret;
  math_rand__ptr_Rand_Shuffle((math_rand_Rand *)math_rand_globalRand, 14999LL, (funcint_comma_int)v16);
  v11 = ret.len + 1;
  array = ret.array;
  if ( ret.cap < (unsigned __int64)(ret.len + 1) )
  {
    *(runtime_slice *)&array = runtime_growslice(ret.array, v11, ret.cap, 1LL, (runtime__type *)&RTYPE_string_0);
    ret.cap = v13;
    ret.array = array;
  }
  ret.len = v11;
  v14 = v11 - 1;
  array[v14].len = 6LL;
  if ( *(_DWORD *)&runtime_writeBarrier.enabled )
    runtime_gcWriteBarrierDX();
  else
    array[v14].str = (uint8 *)"UgandaWanchoWeightWindowYezidi[0][0][]byte\\ufffd\n    \tacceptactionactiveallow";
  return ret.array;
}
```