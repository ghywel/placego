/* rule30_tm6b.c: TM6b, N_6 on every rooted history, continuing TM6's lockstep search at common period Q = 32 past the
 * minimum until every live walk has entered period 64 or the wall cap fires (Local's run; claimed in CLOUD-LOCAL.md,
 * with these predictions pushed before the program was run).
 *
 * RUN-ON:  cpu (C, one thread)
 * BUILD:   cc -O2 -o rule30_tm6b tests/probes/lexicon/rule30_tm6b.c   (binary and transcript outside Git)
 * COMMAND: ./rule30_tm6b [WALL_SECONDS=10800] > transcript
 * COST:    hours expected; caps: WALL_SECONDS of wall time, checked at completed rounds, and 4,096 walks.
 *
 * Domain, walk, children, branch rule and literal check exactly as rule30_tm6.c (common period 32 from the root,
 * lockstep rounds of 2^24 depths). The difference: an exit no longer stops the run; each walk (one history up to
 * rotation; a genuine branch spawns a sibling walk) is followed to its own odd zero. Guards from GPT's GC288, in code:
 * certification requires literal_fail = 0 and the event controls; the only certified frontier is the end of the last
 * COMPLETED round (a walk-cap stop inside a round falls back to the previous round's end); exits observed in an
 * unfinished round are reported as provisional.
 *
 * PREDICTIONS, Local's, published before the run (blind unless marked):
 *   T6b-C1 (control): TM6's events recur: the 15 period-16 branches, the 16 entries to period 32 as doublings, and
 *          the first 32-bit zero anywhere at depth 65,821,412, an odd zero (exit) on the walk from 667,052.
 *   T6b-C2 (control): literal_fail = 0 (required for any certified number).
 *   T6b-P1 (blind, uncertain): within the cap, at least 12 of the 15 histories still in period 32 after TM6 reach
 *          period 64 (counting each original walk's own path, which follows the first child at its branches).
 *   T6b-P2 (blind): at least one genuine branch occurs at period 32 before the cap.
 *   T6b-U (the unexpected check, blind): the total number of 32-bit zeros met, divided by the total walk steps at
 *          period 32 (each walk counted from its own entry to period 32), lies within a factor 2 of 2^-32 (the rough
 *          return estimate behind TM6's prediction).
 * Transcripts go outside Git; the outcome is written into this header by hand after the single run.
 *
 * OUTCOME, 2026-10-07 (M5, one run of the program at c9b160c, 15:03:46 to 18:03:50; transcript outside Git). STOP at
 * the wall cap at a completed round: every live walk has N_6 > 26,424,115,200; 17 of 73 walks live; 56 exits; 72
 * genuine branches (15 at period 16, 57 at period 32); 20 doublings; zeros32 113 over 436,983,015,918 period-32
 * nonzero steps; literal_fail 0. T6b-C1 PASS (TM6's 15 branches and 16 entries recur, and its first 32-bit zero, the
 * exit at 65,821,412 on walk 9). T6b-C2 PASS (no literal failure). Scored as GPT's GC302/GC303 asked: T6b-P1 HELD,
 * 15 of the 15 original walks (IDs 0..15 except 9, each on its first child at later branches) entered period 64, the
 * last (walk 7) at 15,969,952,673; T6b-P2 HELD (57 genuine period-32 branches); T6b-U HELD under GC302's estimand,
 * zeros per nonzero tree step (shared prefixes once, exits censored) = 1.11 x 2^-32. GPT's GC304 counter identities
 * hold on every completed-round line and at the stop (73 = 1 + 72, 17 = 73 - 56, 113 = 72 - 15 + 56). The 56 exit
 * depths give N_6 from 65,821,413 to 26,207,185,419; the seventeen histories still live have N_6 > 26,424,115,200,
 * that is R_6 > 412,876,800, so the period-32 stage of the rooted tree is not complete at the cap.
 *
 * CERTIFICATE (added 2026-10-07 after GPT's GC329; transcribed from the run's transcript into this compact form, all events above depth
 * 399; ids are walk ids, drivers 32-bit words with time 0 in the low bit; N_6 = exit depth + 1):
 * BRANCHES depth:walk>spawned:driver (72):
 *   53207:0>1:3392195120 58286:0>2:467475421 72575:1>3:4200266330 165748:3>4:2455933538 174449:4>5:841757228
 *   179399:4>6:2253686356 243767:5>7:2471531344 350243:5>8:3186540014 445474:8>9:937179100 482608:8>10:1313689165
 *   603582:8>11:628893052 485619:9>12:1665885003 537692:9>13:2698289364 563842:13>14:3520254418
 *   760454:13>15:4181129526 1256211399:1>16:1583773356 1420878968:2>17:3703486136 1836451792:16>18:2629921546
 *   2827536610:16>19:2857867927 2847177602:8>20:1404154146 3340408059:2>21:4048966537 3642208860:3>22:97297938
 *   3786215535:16>23:3136896062 4362050103:23>24:638825238 4422215202:11>25:3295730770 4838002227:8>26:2389950418
 *   4989445007:2>27:3025079060 5709849434:18>28:475437486 6175462563:8>29:147969152 6715102665:8>30:3512954449
 *   6971094751:8>31:196708283 7365035610:28>32:3634197972 8429393530:21>33:4096628558 8754486431:2>34:2604820658
 *   8857887055:14>35:2701686327 9084397203:30>36:1814115415 9124792081:5>37:814436629 9595980363:2>38:227364979
 *   9704789688:36>39:1599569280 11072101718:35>40:1043744899 11390529388:40>41:1745805526
 *   11477974327:33>42:942764514 11579374739:22>43:2894957341 11711978559:27>44:703727086 11728892141:38>45:859392907
 *   12017433514:45>46:848175997 12036933782:37>47:571716184 12809828215:43>48:2171999282 12941372229:29>49:232998782
 *   14006277544:38>50:1360194925 14021636657:37>51:454141283 15129680494:32>52:1842884112
 *   15284077704:38>53:3575956490 15357328367:47>54:407351469 15458055165:47>55:1664370308
 *   15565595922:7>56:1678680239 15768787788:56>57:2822615374 15910195371:51>58:3310834525
 *   16140859095:37>59:2646929115 17165200527:32>60:711861277 19442954235:46>61:616895608
 *   20082646901:45>62:1138832107 22030474216:47>63:2380557267 22455351688:45>64:2430657891
 *   22759750212:46>65:2175102431 23255344970:29>66:797052146 23416550851:62>67:160574630
 *   23437868937:61>68:1658053624 24358923845:62>69:4281023445 24720368155:61>70:1418113572
 *   25042075039:37>71:3020789003 25406592951:45>72:1691507337
 * DOUBLINGS 16 -> 32, depth:walk (16):
 *   229337:0 291256:1 87866:2 183183:3 196188:4 551909:5 271595:6 253536:7 634885:8 667051:9 527723:10 645654:11
 *   555812:12 770531:13 575210:14 894234:15
 * EXITS to period 64, depth:walk:driver (56):
 *   65821412:9:3864731681 105967839:6:3355536448 1325015892:10:1360050466 1555756633:4:2400253140
 *   2107985254:17:2031565668 3438290728:19:3535315323 4251116778:15:1535098249 4513700540:25:724365224
 *   4764963092:12:571995496 4794893267:13:86947585 5548351396:24:3614362437 5808076542:1:4192597603
 *   5860340283:26:99840089 5970036016:20:2711290118 6027773216:3:2582704987 7471047308:0:3753418549
 *   7494387237:28:42864394 7677636034:18:3489176367 7794934634:23:2294105867 7888506455:31:3892237285
 *   9906229075:36:461490179 9958700504:2:2150620435 10159211419:39:717795340 10231753820:30:3131585536
 *   10416313032:14:946747357 11112018386:35:863988310 11471880575:11:3878996005 11619947283:41:4173256340
 *   12436448213:5:530928659 12607541499:33:4210881234 12865517830:43:3699237541 13269780428:8:1018440551
 *   13595453141:42:2512868028 13683521195:16:2054622297 13775976047:34:1644847749 14370559155:49:2654795342
 *   15331293940:40:2717138001 15743373586:54:3737760449 15969952672:7:566798728 15976018535:56:22701242
 *   16474574360:22:1528856250 17306251014:52:720841705 18353953477:44:4036599942 18852065070:53:1628657024
 *   19261032570:55:3153618408 19406865932:21:686389671 19916610114:58:2366369640 20661936806:32:118640460
 *   21375599807:57:3264167146 21776714255:50:4028848408 21841891930:60:1719754840 22959954647:65:3352462195
 *   23985669659:47:3329877940 25452691307:38:499569651 26021394345:46:3364731483 26207185418:29:1757749245
 * LIVE at the stop, walk<parent, all at depth 26,424,115,200 (17):
 *   27<2 37<5 45<38 48<43 51<37 59<37 61<46 62<45 63<47 64<45 66<29 67<62 68<61 69<62 70<61 71<37 72<45
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAXW 4096
#define ROUND (1LL << 24)

typedef struct { uint32_t x, y; int64_t d; int id, parent, p32; } walk_t;   /* p32: past its entry to period 32 */

static walk_t W[MAXW];
static int nw = 0, next_id = 0;
static long long literal_fail = 0;

static inline uint32_t rotr(uint32_t w, int k) { k &= 31; return k ? (w >> k) | (w << (32 - k)) : w; }

static inline uint32_t child_nonzero(uint32_t a, uint32_t b) {
    int t0 = __builtin_ctz(b), t = (t0 + 1) & 31;
    uint32_t c = 0, ct = ((a >> t0) & 1) ^ 1;
    for (int i = 0; i < 32; i++) {
        c |= ct << t;
        uint32_t nt = ((a >> t) & 1) ^ (((b >> t) | ct) & 1);
        t = (t + 1) & 31;
        ct = nt;
    }
    return c;
}

static int is_rot(uint32_t u, uint32_t v) {
    for (int k = 1; k < 32; k++) if (rotr(u, k) == v) return 1;
    return 0;
}

int main(int argc, char **argv) {
    double wall_cap = argc > 1 ? atof(argv[1]) : 10800.0;
    time_t t_start = time(0);
    W[nw++] = (walk_t){0, 0xFFFFFFFFu, 0, next_id++, -1, 0};
    if (argc > 3) {                                 /* smoke tests only: a non-rooted start pair (X, Y) at depth 0 */
        W[0].x = (uint32_t)strtoul(argv[2], 0, 10);
        W[0].y = (uint32_t)strtoul(argv[3], 0, 10);
        printf("SMOKE start (%u, %u): not a rooted run\n", W[0].x, W[0].y);
    }
    int64_t round_end = 0;
    int64_t best = -1;
    long long branches = 0, doublings = 0;
    long long zeros32 = 0, steps32 = 0, exits = 0;
    int64_t last_complete = 0;
    printf("TM6b start: Q = 32, round %lld, wall cap %.0f s\n", (long long)ROUND, wall_cap);
    fflush(stdout);
    for (;;) {
        round_end += ROUND;
        for (int i = 0; i < nw; i++) {             /* nw may grow inside the round: spawned walks run to round_end */
            walk_t *w = &W[i];
            if (w->d < 0) continue;                 /* exited */
            uint32_t x = w->x, y = w->y;
            int64_t d = w->d;
            while (d < round_end) {
                if (y) {
                    if (w->p32) steps32++;
                    uint32_t c = child_nonzero(x, y);
                    if (rotr(c, 1) != (x ^ (y | c))) literal_fail++;
                    x = y; y = c; d++;
                    continue;
                }
                if (w->p32) zeros32++;
                if (__builtin_popcount(x) & 1) {    /* odd: no 32-periodic child; period 64 from d + 1 */
                    printf("EVENT %lld exit walk %d parent %d driver %u N_6 %lld\n", (long long)d, w->id, w->parent, x,
                           (long long)d + 1);
                    exits++;
                    if (best < 0 || d < best) best = d;
                    d = -1;
                    break;
                }
                uint32_t c1 = 0, run = 0;
                for (int t = 0; t < 32; t++) { c1 |= run << t; run ^= (x >> t) & 1; }
                uint32_t c2 = ~c1;
                if (rotr(c1, 1) != (x ^ c1) || rotr(c2, 1) != (x ^ c2)) literal_fail++;
                if (is_rot(c1, c2)) {
                    doublings++;
                    if (d > 399) { printf("EVENT %lld doubling walk %d\n", (long long)d, w->id); w->p32 = 1; }
                } else {
                    branches++;
                    printf("EVENT %lld branch walk %d spawns %d driver %u\n", (long long)d, w->id, next_id, x);
                    if (nw >= MAXW) {
                        printf("STOP walk cap inside a round; certified frontier: N_6 > %lld on every live walk "
                               "(last completed round); exits in this round are provisional; literal_fail %lld\n",
                               (long long)last_complete, literal_fail);
                        fflush(stdout);
                        return 2;
                    }
                    W[nw++] = (walk_t){0, c2, d + 1, next_id++, w->id, w->p32};
                    w = &W[i];                      /* W is static; the pointer stays valid, refreshed for clarity */
                }
                x = 0; y = c1; d++;
            }
            w->x = x; w->y = y; w->d = d;
        }
        last_complete = round_end;
        int live = 0;
        for (int i = 0; i < nw; i++) live += W[i].d >= 0;
        double el = difftime(time(0), t_start);
        if ((round_end & ((1LL << 30) - 1)) == 0 || live == 0)
            printf("PROGRESS depth %lld live %d walks %d exits %lld branches %lld doublings %lld zeros32 %lld "
                   "steps32 %lld literal_fail %lld elapsed %.0f s\n", (long long)round_end, live, nw, exits, branches,
                   doublings, zeros32, steps32, literal_fail, el);
        fflush(stdout);
        if (live == 0) {
            printf("RESULT every walk entered period 64 by depth %lld; walks %d; zeros32 %lld; steps32 %lld; "
                   "literal_fail %lld (%s)\n", (long long)round_end, nw, zeros32, steps32, literal_fail,
                   literal_fail ? "INVALID: literal failures" : "certified if the event controls pass");
            return literal_fail ? 4 : 0;
        }
        if (el > wall_cap) {
            printf("STOP wall cap at a completed round: every live walk has N_6 > %lld; live %d of %d walks; exits "
                   "%lld; zeros32 %lld; steps32 %lld; literal_fail %lld (%s)\n", (long long)round_end, live, nw,
                   exits, zeros32, steps32, literal_fail,
                   literal_fail ? "INVALID: literal failures" : "certified if the event controls pass");
            for (int i = 0; i < nw; i++)
                if (W[i].d >= 0) printf("LIVE walk %d parent %d depth %lld\n", W[i].id, W[i].parent, (long long)W[i].d);
            return literal_fail ? 4 : 3;
        }
    }
}
