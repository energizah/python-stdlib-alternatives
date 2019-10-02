import pathlib
import textwrap


def main(stdlib_path, alternatives_path, header_path, output_path):
    alternatives = {}
    stdlib_to_alternatives = {}

    alternatives_path = pathlib.Path(alternatives_path)
    alternatives_path.write_text(
        "\n".join(sorted(alternatives_path.read_text().splitlines())) + "\n"
    )

    for line in alternatives_path.read_text().splitlines():
        name, url, description = line.split(maxsplit=2)
        assert url.startswith("http")
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
            stdlib_module_link = (
                f"https://docs.python.org/3/library/{stdlib_module}.html"
            )
            stdlib_module_text = f"[{stdlib_module}]({stdlib_module_link})"
            section = f"### {stdlib_module_text}\n" + alts_text
            out.append(section)

    out_text = pathlib.Path(header_path).read_text() + "\n".join(out)
    pathlib.Path(output_path).write_text(out_text)


if __name__ == "__main__":
    main(
        stdlib_path="input/stdlib.txt",
        alternatives_path="input/alternatives.txt",
        header_path="input/header.md",
        output_path="README.md",
    )
