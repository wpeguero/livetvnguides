import streamlink

M3U = "#EXTM3U\n"
na = "https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u"


def main():
    print(M3U)
    with open("channel_info.txt") as f:
        quality = "best"
        for line in f:
            line = line.strip()
            if not line or line.startswith("~~"):
                continue
            if not line.startswith("http"):
                line = line.split("|")
                ch_name = line[0].strip()
                grp_title = line[1].strip().title()
                tvg_logo = line[2].strip()
                tvg_id = line[3].strip()
                quality = line[4].strip()
                print(
                    f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}'
                )
            else:
                grab(line, quality)


def grab(link: str, quality: str):
    """Extract the url link to view the show."""
    session = streamlink.Streamlink()
    streams = session.streams(link)
    try:
        best = streams["best"].url
        if "youtube" in link:
            pass
        else:
            if "live-720.m3u" in best:
                best = best.replace("live-720.m3u", f"live-{quality}.m3u")
            elif "live-240.m3u" in best:
                best = best.replace("live-240.m3u", f"live-{quality}.m3u")
            elif "live-380.m3u" in best:
                best = best.replace("live-380.m3u", f"live-{quality}.m3u")
            else:
                pass
    except KeyError as e:
        best = na
        print(e)
    print(f"{best}")


main()
