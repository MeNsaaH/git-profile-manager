import configparser


class ConfigParser(configparser.ConfigParser):
    """ Config Parser that writes in git format """

    def _write_section(self, fp, section_name, section_items, delimiter, indent_values=2):
        """Write a single section to the specified `fp'."""

        if len(section_items) == 0:
            return
        indent = " " * indent_values
        fp.write("[{}]\n".format(section_name))
        for key, value in section_items:
            value = self._interpolation.before_write(self, section_name, key,
                                                     value)
            if value is not None or not self._allow_no_value:
                value = delimiter + str(value).replace('\n', '\n\t')
            else:
                value = ""
            fp.write("{}{}{}\n".format(indent,key, value))
        fp.write("\n")
