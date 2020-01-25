{! NOTE: Markdown is a whitespace-sensitive language. As a result, this file requires
manual whitespace insertion. Use {~n} for newlines and {~s} for spaces.!}

{#entry.loaded_parts}
{^data_idx}
{! non-data parts, sheer markdown text !}
{content}
{:else}
## {ordinal_text} {title}
{~n}{~n}
{#attrs}
{@eq key=type value="default"}
   * {title}: {value}
   {@sep}{~n}{/sep}
{/eq}
{/attrs}
{#links}
   * {#value}[{title}]({href}{?tip} "{tip}"{/tip}){/value}
      {! TODO: tip quote escaping !}
{@sep}{~n}{/sep}
{/links}
{~n}
{content}
{/data_idx}
{~n}{~n}---{~n}{~n}
{/entry.loaded_parts}
