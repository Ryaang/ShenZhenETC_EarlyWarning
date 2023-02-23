(self["webpackChunkpart_time_job"] = self["webpackChunkpart_time_job"] || []).push([[443], {
    126: (t, a, e) => {
        "use strict";
        e.r(a), e.d(a, {default: () => o});
        var i = function () {
            var t = this, a = t._self._c;
            return a("div", {staticClass: "H15-1216-500"}, [a("div", {staticClass: "operate"}, [a("el-form", {
                ref: "form",
                staticClass: "demo-form-inline",
                attrs: {inline: !0, model: t.searchForm}
            }, [a("el-form-item", {attrs: {label: "CX", prop: "CX"}}, [a("el-select", {
                attrs: {
                    filterable: "",
                    placeholder: "CX",
                    clearable: ""
                }, model: {
                    value: t.searchForm.CX, callback: function (a) {
                        t.$set(t.searchForm, "CX", a)
                    }, expression: "searchForm.CX"
                }
            }, t._l(t.CX_OPTION, (function (t, e) {
                return a("el-option", {key: e, attrs: {label: t, value: t}})
            })), 1)], 1), a("el-form-item", {
                attrs: {
                    label: "SFZCKMC",
                    prop: "SFZCKMC"
                }
            }, [a("el-select", {
                attrs: {filterable: "", placeholder: "SFZCKMC", clearable: ""},
                model: {
                    value: t.searchForm.SFZCKMC, callback: function (a) {
                        t.$set(t.searchForm, "SFZCKMC", a)
                    }, expression: "searchForm.SFZCKMC"
                }
            }, t._l(t.SFZCKMC_OPTION, (function (t, e) {
                return a("el-option", {key: e, attrs: {label: t, value: t}})
            })), 1)], 1), a("el-form-item", {
                attrs: {
                    label: "SFZRKMC",
                    prop: "SFZRKMC"
                }
            }, [a("el-select", {
                attrs: {filterable: "", placeholder: "SFZRKMC", clearable: ""},
                model: {
                    value: t.searchForm.SFZRKMC, callback: function (a) {
                        t.$set(t.searchForm, "SFZRKMC", a)
                    }, expression: "searchForm.SFZRKMC"
                }
            }, t._l(t.SFZRKMC_OPTION, (function (t, e) {
                return a("el-option", {key: e, attrs: {label: t, value: t}})
            })), 1)], 1), a("el-form-item", {attrs: {label: "BZ", prop: "BZ"}}, [a("el-select", {
                attrs: {
                    filterable: "",
                    placeholder: "BZ",
                    clearable: ""
                }, model: {
                    value: t.searchForm.BZ, callback: function (a) {
                        t.$set(t.searchForm, "BZ", a)
                    }, expression: "searchForm.BZ"
                }
            }, t._l(t.BZ_OPTION, (function (t, e) {
                return a("el-option", {key: e, attrs: {label: t, value: t}})
            })), 1)], 1), a("el-form-item", {
                attrs: {
                    label: "startXH",
                    prop: "startXH"
                }
            }, [a("el-select", {
                attrs: {filterable: "", placeholder: "startXH", clearable: ""},
                model: {
                    value: t.searchForm.startXH, callback: function (a) {
                        t.$set(t.searchForm, "startXH", a)
                    }, expression: "searchForm.startXH"
                }
            }, t._l(t.startXH_OPTION, (function (t, e) {
                return a("el-option", {key: e, attrs: {label: t, value: t}})
            })), 1)], 1), a("el-form-item", {
                attrs: {
                    label: "timeRange",
                    prop: "timeRange"
                }
            }, [a("el-date-picker", {
                attrs: {
                    type: "datetimerange",
                    "value-format": "yyyy-MM-dd HH:mm:ss",
                    "range-separator": "至",
                    "start-placeholder": "开始日期",
                    "end-placeholder": "结束日期"
                }, model: {
                    value: t.searchForm.timeRange, callback: function (a) {
                        t.$set(t.searchForm, "timeRange", a)
                    }, expression: "searchForm.timeRange"
                }
            })], 1), a("el-form-item", {
                attrs: {
                    label: "filetype",
                    prop: "filetype"
                }
            }, [a("el-select", {
                attrs: {filterable: "", placeholder: "filetype", clearable: ""},
                model: {
                    value: t.searchForm.filetype, callback: function (a) {
                        t.$set(t.searchForm, "filetype", a)
                    }, expression: "searchForm.filetype"
                }
            }, t._l(t.filetype_OPTION, (function (t, e) {
                return a("el-option", {key: e, attrs: {label: t, value: t}})
            })), 1)], 1), a("el-form-item", [a("el-button", {
                attrs: {type: "primary"},
                on: {click: t.onSearch}
            }, [t._v("查询")])], 1), a("el-form-item", [a("el-button", {
                attrs: {type: "primary"},
                on: {click: t.onReset}
            }, [t._v("重置")])], 1), a("el-form-item", [a("el-button", {
                attrs: {type: "primary"},
                on: {click: t.onDownLoad}
            }, [t._v("下载")])], 1)], 1)], 1), a("el-table", {
                staticStyle: {width: "100%"},
                attrs: {data: t.tableData, stripe: "", border: "", height: "calc(100% - 120px)"}
            }, [a("el-table-column", {attrs: {prop: "XH", label: "XH"}}), a("el-table-column", {
                attrs: {
                    prop: "CX",
                    label: "CX"
                }
            }), a("el-table-column", {attrs: {prop: "CP", label: "CP"}}), a("el-table-column", {
                attrs: {
                    prop: "SFZRKMC",
                    label: "SFZRKMC"
                }
            }), a("el-table-column", {
                attrs: {
                    prop: "RKSJ",
                    label: "RKSJ"
                }
            }), a("el-table-column", {
                attrs: {
                    prop: "SFZCKMC",
                    label: "SFZCKMC"
                }
            }), a("el-table-column", {attrs: {prop: "CKSJ", label: "CKSJ"}}), a("el-table-column", {
                attrs: {
                    prop: "BZ",
                    label: "BZ"
                }
            })], 1), a("div", {staticClass: "pagination"}, [a("el-pagination", {
                attrs: {
                    layout: "total, prev, pager, next",
                    "page-size": t.pageSize,
                    total: t.total
                }, on: {"current-change": t.handleCurrentChange}
            })], 1)], 1)
        }, n = [];
        e(21249), e(41539), e(70189), e(78783), e(33948), e(47042);
        const A = {
            data: function () {
                return {
                    CX_OPTION: [],
                    SFZCKMC_OPTION: [],
                    SFZRKMC_OPTION: [],
                    BZ_OPTION: [],
                    startXH_OPTION: [1e3, 2e3, 3e3, 4e3, 5e3, 6e3, 7e3, 8e3, 9e3, 1e4, 11e3, 12e3, 13e3, 14e3, 15e3, 16e3, 17e3, 18e3, 19e3, 2e4],
                    filetype_OPTION:["csv","xlsx"],
                    searchForm: {CX: "", SFZCKMC: "", SFZRKMC: "", BZ: "", startXH: "", timeRange: null,filetype:""},
                    rawData: [],
                    tableData: [],
                    total: 0,
                    pageSize: 100
                }
            }, created: function () {
                this.initTableData()
            }, methods: {
                initTableData: function () {
                    var t = this, a = {cond: {}, field: [], filetype: ""}, e = this.searchForm, i = e.CX,
                        n = e.SFZCKMC, A = e.SFZRKMC, r = e.BZ, s = e.startXH, l = e.timeRange,k=e.filetype;
                    i && (a.cond.CX = i), n && (a.cond.SFZCKMC = n), A && (a.cond.SFZRKMC = A), r && (a.cond.BZ = r), s && (a.cond.startXH = s), k && (a.filetype = k), l && 2 === l.length && (a.cond.RKSJ = l), this.axios.post("/api/interactive", a).then((function (a) {
                        var e = a.data;
                        t.rawData = e.map((function (t) {
                            return {
                                XH: t[0],
                                CP: t[1],
                                CX: t[2],
                                SFZRKMC: t[3],
                                RKSJ: t[4],
                                SFZCKMC: t[5],
                                CKSJ: t[6],
                                BZ: t[7]
                            }
                        })), t.total = e.length, t.handleCurrentChange(1), t.CX_OPTION = new Set(t.rawData.map((function (t) {
                            return t.CX
                        }))), t.SFZCKMC_OPTION = new Set(t.rawData.map((function (t) {
                            return t.SFZCKMC
                        }))), t.SFZRKMC_OPTION = new Set(t.rawData.map((function (t) {
                            return t.SFZRKMC
                        }))), t.BZ_OPTION = new Set(t.rawData.map((function (t) {
                            return t.BZ
                        })))
                    }))
                }, handleCurrentChange: function (t) {
                    var a = (t - 1) * this.pageSize, e = t * this.pageSize;
                    this.tableData = this.rawData.slice(a, e)
                }, onSearch: function () {
                    this.initTableData()
                }, onReset: function () {
                    this.$refs.form.resetFields(), this.initTableData()
                }, onDownLoad: function (t) {
                    window.open("http://124.71.207.74:5000/download", "_blank")
                }
            }
        }, r = A;
        var s = e(1001), l = (0, s.Z)(r, i, n, !1, null, "2fea7e1a", null);
        const o = l.exports
    }, 15687: (t, a, e) => {
        "use strict";
        e.r(a), e.d(a, {default: () => c});
        e(68309);
        var i = function () {
            var t = this, a = t._self._c;
            return a("div", {staticClass: "Z39-1216-800"}, [a("div", {
                staticClass: "paintContainer",
                style: {width: t.width + "px"}
            }, [a("div", {staticClass: "paintTool"}, [a("div", {staticClass: "paintShape"}, t._l(t.paintShapeList, (function (e, i) {
                return a("div", {
                    key: i, class: {active: e.name === t.radio2}, on: {
                        click: function (a) {
                            t.radio2 = e.name
                        }
                    }
                }, [a("el-tooltip", {
                    attrs: {
                        effect: "dark",
                        content: e.name,
                        placement: "top",
                        "open-delay": 500
                    }
                }, [a("img", {attrs: {src: e.imgUrl}})])], 1)
            })), 0), a("div", {staticClass: "inputNumber"}, [a("el-radio-group", {
                attrs: {size: "mini"},
                model: {
                    value: t.radio1, callback: function (a) {
                        t.radio1 = a
                    }, expression: "radio1"
                }
            }, [a("el-radio-button", {attrs: {label: "填充"}}), a("el-radio-button", {attrs: {label: "轮廓"}})], 1), a("div", {staticClass: "label"}, [t._v("绘画样式")])], 1), a("div", {staticClass: "inputNumber paintColor"}, [a("el-color-picker", {
                staticClass: "colorPicker",
                attrs: {size: "mini"},
                model: {
                    value: t.color1, callback: function (a) {
                        t.color1 = a
                    }, expression: "color1"
                }
            }), a("div", {staticClass: "label"}, [t._v("颜色")])], 1), a("div", {staticClass: "inputNumber"}, [a("el-input-number", {
                attrs: {
                    size: "mini",
                    min: 1,
                    max: 30
                }, model: {
                    value: t.lineWidth, callback: function (a) {
                        t.lineWidth = a
                    }, expression: "lineWidth"
                }
            }), a("div", {staticClass: "label"}, [t._v("画笔粗细")])], 1), a("div", {staticClass: "inputNumber"}, [a("el-input-number", {
                attrs: {
                    size: "mini",
                    min: 1,
                    max: 30
                }, model: {
                    value: t.cornerRadius, callback: function (a) {
                        t.cornerRadius = a
                    }, expression: "cornerRadius"
                }
            }), a("div", {staticClass: "label"}, [t._v("圆角矩形半径")])], 1), a("div", {staticClass: "inputNumber"}, [a("el-input-number", {
                attrs: {
                    size: "mini",
                    min: 3,
                    max: 30
                }, model: {
                    value: t.polyNum, callback: function (a) {
                        t.polyNum = a
                    }, expression: "polyNum"
                }
            }), a("div", {staticClass: "label"}, [t._v("多边形边数")])], 1)]), a("div", {staticClass: "paintArea"}, [a("el-card", {staticClass: "box-card"}, [a("div", {
                staticClass: "header",
                attrs: {slot: "header"},
                slot: "header"
            }, [a("span", [t._v(" 画板区域 "), a("i", [t._v("（" + t._s(t.width + " * " + t.height) + "）")])]), a("el-button", {
                attrs: {type: "text"},
                on: {click: t.setTheWaterMark}
            }, [t._v("设置水印")]), a("el-button", {
                attrs: {type: "text"},
                on: {click: t.clearArtBoard}
            }, [t._v("清空")]), a("el-button", {
                attrs: {type: "text"},
                on: {click: t.displayToImage}
            }, [t._v("储存")])], 1), a("canvas", {
                ref: "paint", attrs: {width: t.width}, on: {
                    mousedown: function (a) {
                        return t.onmousedown(a)
                    }
                }
            })])], 1)]), a("div", {
                staticClass: "imageContainer",
                style: {width: "calc(100% - ".concat(t.width + 10, "px)")}
            }, [a("el-card", {staticClass: "saveImageArea"}, [a("div", {
                attrs: {slot: "header"},
                slot: "header"
            }, [a("span", [t._v("生成图片")]), a("el-button", {
                staticStyle: {float: "right", padding: "3px 0"},
                attrs: {type: "text"},
                on: {click: t.clearToImage}
            }, [t._v("清空")])], 1), t._l(t.imgBase60Data, (function (e, i) {
                return a("el-card", {staticClass: "saveImageCard"}, [a("el-image", {
                    staticStyle: {
                        width: "100px",
                        height: "100px"
                    }, attrs: {src: e, "preview-src-list": [e]}
                }), a("i", {
                    staticClass: "el-icon-delete", on: {
                        click: function (a) {
                            return t.deleteImage(i)
                        }
                    }
                }), a("i", {
                    staticClass: "el-icon-download", on: {
                        click: function (a) {
                            return t.saveToImage(e)
                        }
                    }
                })], 1)
            })), a("el-statistic", {
                attrs: {
                    value: t.deadline2,
                    format: "HH:mm:ss",
                    "time-indices": "",
                    title: "剩余绘画时间"
                }, on: {finish: t.hilarity}
            })], 2), a("el-card", {staticClass: "importImageArea"}, [a("div", {
                attrs: {slot: "header"},
                slot: "header"
            }, [a("span", [t._v("上传图片预览")]), a("el-upload", {
                staticClass: "uploadImage",
                attrs: {
                    action: "",
                    "http-request": t.httpRequest,
                    "before-upload": t.beforeUploadClick,
                    limit: 30,
                    multiple: "",
                    "show-file-list": !1
                }
            }, [a("el-button", {
                attrs: {
                    size: "small",
                    type: "text"
                }
            }, [t._v("点击上传")])], 1)], 1), t._l(t.uploadImageBase64Data, (function (e, i) {
                return a("el-card", {staticClass: "uploadImageCard"}, [a("el-image", {
                    staticStyle: {
                        width: "100px",
                        height: "100px"
                    }, attrs: {src: e.base64Url, "preview-src-list": [e.base64Url]}
                }), a("el-rate", {
                    model: {
                        value: e.value, callback: function (a) {
                            t.$set(e, "value", a)
                        }, expression: "item.value"
                    }
                })], 1)
            }))], 2)], 1)])
        }, n = [];
        e(3843), e(83710), e(43290), e(57658), e(74916), e(4723), e(96647), e(75505), e(87714), e(82801), e(1174), e(39575), e(41539), e(82472), e(48675), e(92990), e(18927), e(33105), e(35035), e(74345), e(7174), e(63408), e(14590), e(32846), e(44731), e(77209), e(96319), e(58867), e(37789), e(33739), e(29368), e(14483), e(12056), e(3462), e(30678), e(27462), e(33824), e(55021), e(12974), e(15016), e(78783), e(33948), e(60285), e(41637), e(40561), e(94986);

        function A(t) {
            return new Promise((function (a, e) {
                var i = new FileReader;
                i.readAsDataURL(t), i.onload = function (t) {
                    a(t.target.result)
                }
            }))
        }

        const r = {
            data: function () {
                return {
                    deadline2: Date.now() + 6e4,
                    paintShapeList: [{name: "绘画", imgUrl: e(64647)}, {name: "直线", imgUrl: e(15121)}, {
                        name: "矩形",
                        imgUrl: e(95980)
                    }, {name: "圆角矩形", imgUrl: e(79761)}, {name: "多边形", imgUrl: e(54484)}, {
                        name: "圆",
                        imgUrl: e(40091)
                    }, {name: "文本", imgUrl: e(82384)}],
                    width: 800,
                    height: 0,
                    canvas: null,
                    paint: null,
                    paintImageData: {},
                    radio1: "轮廓",
                    radio2: "绘画",
                    radio3: "纯色",
                    color1: "#dc1b1b",
                    color2: "#8493a3",
                    lineWidth: 1,
                    cornerRadius: 20,
                    polyNum: 6,
                    imgBase60Data: [],
                    uploadImageBase64Data: []
                }
            }, mounted: function () {
                var t = this;
                this.canvas = this.$refs.paint, this.paint = this.$refs.paint.getContext("2d"), this.canvas.height = document.body.clientHeight - 208, this.height = document.body.clientHeight - 208, this.paint.beginPath(), this.paint.fillStyle = "#fff", this.paint.fillRect(0, 0, this.canvas.width, this.canvas.height), this.paint.closePath(), window.onresize = function () {
                    t.canvas.height = document.body.clientHeight - 208, t.height = document.body.clientHeight - 208, t.paintImageData.hasOwnProperty("data") && t.paint.putImageData(t.paintImageData, 0, 0)
                }
            }, methods: {
                onmousedown: function (t) {
                    var a = this, e = t.offsetX, i = t.offsetY;
                    "绘画" === this.radio2 && (this.paint.clearRect(0, 0, this.width, this.height), this.paintImageData.hasOwnProperty("data") && this.paint.putImageData(this.paintImageData, 0, 0), this.paint.beginPath(), this.paint.moveTo(e, i)), this.$refs.paint.onmousemove = function (t) {
                        var n = t.offsetX, A = t.offsetY;
                        switch (a.paint.clearRect(0, 0, a.width, a.height), a.paintImageData.hasOwnProperty("data") && a.paint.putImageData(a.paintImageData, 0, 0), a.radio2) {
                            case"绘画":
                                a.paintMousePath(n, A);
                                break;
                            case"直线":
                                a.paintLine(e, i, n, A);
                                break;
                            case"矩形":
                                a.paintRectangle(e, i, n, A);
                                break;
                            case"圆角矩形":
                                a.paintRoundedRectangle(e, i, n, A);
                                break;
                            case"多边形":
                                a.paintPolygon(e, i, n, A);
                                break;
                            case"圆":
                                a.paintCircle(e, i, n, A);
                                break
                        }
                    }, this.$refs.paint.onmouseup = function (t) {
                        if (a.$refs.paint.onmousemove = null, "文本" === a.radio2) {
                            var n = window.prompt("请输入文字");
                            n && a.paintText(n, e, i)
                        }
                        "绘画" === a.radio2 && a.paint.closePath(), a.paintImageData = a.paint.getImageData(0, 0, a.width, a.height)
                    }
                }, paintMousePath: function (t, a) {
                    this.paint.lineTo(t, a), this.paint.lineWidth = this.lineWidth, this.paint.strokeStyle = this.color1, this.paint.stroke()
                }, paintLine: function (t, a, e, i) {
                    this.paint.beginPath(), this.paint.moveTo(t, a), this.paint.lineTo(e, i), this.paint.lineWidth = this.lineWidth, this.paint.strokeStyle = this.color1, this.paint.stroke(), this.paint.closePath()
                }, paintRectangle: function (t, a, e, i) {
                    switch (this.paint.beginPath(), this.paint.lineWidth = this.lineWidth, this.radio1) {
                        case"轮廓":
                            this.paint.strokeStyle = this.color1, this.paint.strokeRect(t, a, e - t, i - a);
                            break;
                        case"填充":
                            this.paint.fillStyle = this.color1, this.paint.fillRect(t, a, e - t, i - a);
                            break
                    }
                    this.paint.closePath()
                }, paintRoundedRectangle: function (t, a, e, i) {
                    switch (this.paint.beginPath(), this.paint.lineWidth = this.lineWidth, this.paint.moveTo(t + this.cornerRadius, a), this.paint.arcTo(e, a, e, a + this.cornerRadius, this.cornerRadius), this.paint.arcTo(e, i, e - this.cornerRadius, i, this.cornerRadius), this.paint.arcTo(t, i, t, i - this.cornerRadius, this.cornerRadius), this.paint.arcTo(t, a, t + this.cornerRadius, a, this.cornerRadius), this.paint.closePath(), this.radio1) {
                        case"轮廓":
                            this.paint.strokeStyle = this.color1, this.paint.stroke();
                            break;
                        case"填充":
                            this.paint.fillStyle = this.color1, this.paint.fill();
                            break
                    }
                }, paintPolygon: function (t, a, e, i) {
                    this.paint.beginPath(), this.paint.lineWidth = this.lineWidth;
                    for (var n = Math.sqrt(Math.pow(e - t, 2) + Math.pow(i - a, 2)), A = 360 / this.polyNum * Math.PI / 180, r = 0; r < this.polyNum; r++) this.paint.lineTo(t + Math.cos(A * r) * n, a + Math.sin(A * r) * n);
                    switch (this.paint.closePath(), this.radio1) {
                        case"轮廓":
                            this.paint.strokeStyle = this.color1, this.paint.stroke();
                            break;
                        case"填充":
                            this.paint.fillStyle = this.color1, this.paint.fill();
                            break
                    }
                }, paintCircle: function (t, a, e, i) {
                    this.paint.beginPath(), this.paint.lineWidth = this.lineWidth;
                    var n = Math.sqrt(Math.pow(e - t, 2) + Math.pow(i - a, 2));
                    switch (this.paint.arc(t, a, n, 0, 2 * Math.PI), this.paint.closePath(), this.radio1) {
                        case"轮廓":
                            this.paint.strokeStyle = this.color1, this.paint.stroke();
                            break;
                        case"填充":
                            this.paint.fillStyle = this.color1, this.paint.fill();
                            break
                    }
                }, paintText: function (t, a, e) {
                    switch (this.paint.font = "20px 宋体 bold", this.paint.textAlign = "left", this.radio1) {
                        case"轮廓":
                            this.paint.strokeStyle = this.color1, this.paint.strokeText(t, a, e);
                            break;
                        case"填充":
                            this.paint.fillStyle = this.color1, this.paint.fillText(t, a, e);
                            break
                    }
                }, setTheWaterMark: function () {
                    var t = this, a = new Image;
                    a.src = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAk4AAAIACAYAAAB0C+PpAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAEISSURBVHhe7d0JuDxVdff7682917zv+3iTXHkzaeIYFFGjGOchaoiKqCCCA0IMCs4KDjiioqIRGQScFURREMQhqIgEBQXiPOAAUTEaHOLE6Xme9l2bXkfO/5xV3Xt3V3VXd30/z/N7PPKvXad77Tp91umu2vV/OAAAAAShcQIAAAhE4wQAABCIxgkAACAQjRMAAEAgGicAAIBANE4AAACBaJwAAAAC0TgBAAAEonECAAAIROMEAAAQiMYJAAAgEI0TAABAIBonAACAQDROAAAAgWicAAAAAtE4AQAABKJxAgAACETjBAAAEIjGCQAAIBCNEwAAQCAaJwAAgEA0TgAAAIFonAAAAALROAEAAASicQIAAAhE4wQAABCIxgkAACAQjRMAAEAgGicAAIBANE4AAACBaJwAAAAC0TgBAAAEonECAAAIROMEAAAQiMYJAAAgEI0TAABAIBonAACAQDROAAAAgWicAAAAAtE4AQAABKJxAgAACETjBAAAEIjGCQAAIBCNEwAAQCAaJwAAgEA0TgAAAIFonAAAAALROAEAAASicQIAAAhE4wQAABCIxgkAACAQjRMAAEAgGicAAIBANE4AAACBaJwAAAAC0TgBAAAEonECAAAIROMEAAAQiMYJAAAgEI0TAABAIBonAACAQDROAAAAgWicAAAAAtE4AQAABKJxAgAACETjBAAAEIjGCQAAIBCNEwAAQCAaJwAAgEA0TgAAAIFonLLSPsm52gHOVfZ07nop86qlfDvnqns713y5PiEAACC/IZGa/relWTrIbkRWPZV7Otf9iD5RAACKSX4jIhWtE+2GY91Sf4o82dH4OQMAUDDymxBza77UbjLWNdWHypPuj587lqtz3vj489onODe4avx1rMHV0vyfJPt6nnONo2W/58h/HI7/LVb3Ezd+xNv6FzlUvjr+Otbwx/KcTpXH83zJi+QxfUD+Y3P8b7G6n5ahx4y/br5eHtMV46+xugb/KfP6YZnP10r8MfLsAueF8rMif7z3LpK/a9taIGRFfgtiLu23283Fuqf+JC0AlqJzrj0vPvV/khfP0AZjJC+6R9j78bmh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", a.onload = function () {
                        var e = a.width, i = a.height;
                        t.paint.beginPath(), t.paint.fillStyle = t.paint.createPattern(a, "repeat"), t.paint.fillRect(t.width - e, t.height - i, t.width, t.height), t.paint.closePath(), t.paintImageData = t.paint.getImageData(0, 0, t.width, t.height)
                    }
                }, clearArtBoard: function () {
                    this.paint.clearRect(0, 0, this.width, this.height), this.paintImageData = {}
                }, displayToImage: function () {
                    if (this.paintImageData.hasOwnProperty("data") && !(this.imgBase60Data.length > 29)) {
                        var t = this.canvas.toDataURL("image/jpeg");
                        this.imgBase60Data.push(t)
                    }
                }, clearToImage: function () {
                    this.imgBase60Data = []
                }, saveCanvasImage: function () {
                    if (this.paintImageData.hasOwnProperty("data")) {
                        var t = this.canvas.toDataURL("image/jpg"), a = t.split(","), e = a[0].match(/:(.*?);/)[1],
                            i = atob(a[1]), n = i.length, A = new Uint8Array(n);
                        while (n--) A[n] = i.charCodeAt(n);
                        var r = new File([A], "filename", {type: e}), s = URL.createObjectURL(r),
                            l = document.createElement("a");
                        l.download = r.name, l.href = s, document.body.appendChild(l), l.click(), document.body.removeChild(l), URL.revokeObjectURL(s)
                    }
                }, deleteImage: function (t) {
                    this.imgBase60Data.splice(t, 1)
                }, saveToImage: function (t) {
                    var a = t.split(","), e = a[0].match(/:(.*?);/)[1], i = atob(a[1]), n = i.length,
                        A = new Uint8Array(n);
                    while (n--) A[n] = i.charCodeAt(n);
                    var r = new File([A], "filename", {type: e}), s = URL.createObjectURL(r),
                        l = document.createElement("a");
                    l.download = r.name, l.href = s, document.body.appendChild(l), l.click(), document.body.removeChild(l), URL.revokeObjectURL(s)
                }, hilarity: function () {
                    this.$notify({title: "提示", message: "时间已到，你可知寸金难买寸光阴？", duration: 0})
                }, beforeUploadClick: function (t) {
                    var a = this;
                    A(t).then((function (t) {
                        a.uploadImageBase64Data.push({base64Url: t, value: null})
                    }))
                }, httpRequest: function (t) {
                }
            }
        }, s = r;
        var l = e(1001), o = (0, l.Z)(s, i, n, !1, null, "6a563753", null);
        const c = o.exports
    }, 75505: (t, a, e) => {
        var i = e(82109), n = e(35005), A = e(1702), r = e(47293), s = e(41340), l = e(92597), o = e(48053),
            c = e(14170).ctoi, p = /[^\d+/a-z]/i, h = /[\t\n\f\r ]+/g, d = /[=]+$/, u = n("atob"),
            f = String.fromCharCode, v = A("".charAt), m = A("".replace), g = A(p.exec), C = r((function () {
                return "" !== u(" ")
            })), b = !r((function () {
                u("a")
            })), k = !C && !b && !r((function () {
                u()
            })), P = !C && !b && 1 !== u.length;
        i({global: !0, enumerable: !0, forced: C || b || k || P}, {
            atob: function (t) {
                if (o(arguments.length, 1), k || P) return u(t);
                var a, e, i = m(s(t), h, ""), A = "", r = 0, C = 0;
                if (i.length % 4 == 0 && (i = m(i, d, "")), i.length % 4 == 1 || g(p, i)) throw new (n("DOMException"))("The string is not correctly encoded", "InvalidCharacterError");
                while (a = v(i, r++)) l(c, a) && (e = C % 4 ? 64 * e + c[a] : c[a], C++ % 4 && (A += f(255 & e >> (-2 * C & 6))));
                return A
            }
        })
    }, 64647: (t, a, e) => {
        "use strict";
        t.exports = e.p + "img/huihua.e869982c.svg"
    }, 15121: (t, a, e) => {
        "use strict";
        t.exports = e.p + "img/line.2d572914.svg"
    }, 95980: (t, a, e) => {
        "use strict";
        t.exports = e.p + "img/xingzhuang-juxing.d34e503d.svg"
    }, 40091: (t, a, e) => {
        "use strict";
        t.exports = e.p + "img/xingzhuang-tuoyuanxing.63967a9a.svg"
    }, 82384: (t, a, e) => {
        "use strict";
        t.exports = e.p + "img/xingzhuang-wenzi.2334eb84.svg"
    }, 54484: (t, a, e) => {
        "use strict";
        t.exports = e.p + "img/xingzhuang-xingxing.3fa4561c.svg"
    }, 79761: (t, a, e) => {
        "use strict";
        t.exports = e.p + "img/yuanjiaojuxing1.f7733513.svg"
    }
}]);
//# sourceMappingURL=about.c291580f.js.map