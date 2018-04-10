 
                    def whichEncode(text):
                        text0 = text[0]
                        try:
                            text0.decode('utf8')
                        except Exception, e:
                            if "unexpected end of data" in str(e):
                                return "utf8"
                            elif "invalid start byte" in str(e):
                                return "gbk_gb2312"
                            elif "ascii" in str(e):
                                return "Unicode"
                        return "utf8"
                 
                    print whichEncode()
                  