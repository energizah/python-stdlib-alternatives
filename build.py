import pathlib
import textwrap


def main(stdlib_path, alternatives_path, output_path):
    alternatives = {}
    stdlib_to_alternatives = {}

    for line in pathlib.Path(alternatives_path).read_text().splitlines():
        name, url, description = line.split(maxsplit=2)
        alternatives[name] = {"description": description, "url": url}

    for line in pathlib.Path(stdlib_path).read_text().splitlines():
        if not line.strip():
            continue
        stdlib_module, *alts = line.split()
        stdlib_to_alternatives[stdlib_module] = alts

    out = []
    for stdlib_module, alternative_names in stdlib_to_alternatives.items():
        if alternative_names:
            alts = []
            for alt_name in alternative_names:
                alt = alternatives[alt_name]
                alt_text = f'- [{alt_name}]({alt["url"]}): {alt["description"]} '
                alts.append(alt_text)
            alts_text = "\n".join(alts) + "\n"
            section = f"### {stdlib_module}\n" + alts_text
            out.append(section)

    pathlib.Path(output_path).write_text("\n".join(out))


if __name__ == "__main__":
    main("stdlib.txt", "alternatives.txt", "README.md")
