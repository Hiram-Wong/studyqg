const app = getApp();
var plugin = requirePlugin("WechatSI")
let manager = plugin.getRecordRecognitionManager()

Page({
  data: {
    arrList: [],
    cardCur: 0,
    swiperList: [],
    isBindExpert: true,
    modalName: null,
    textareaValue: '',
    sayImg:'/images/say.png',
    SearchTypeValue: false,
    ClipboardValue: '',
    ClipboardType: false,
    loadProgress:0,
    CustomBar: app.globalData.CustomBar
  },
  streamRecord: function () {
    manager.start({
      lang: 'zh_CN',
      duration: 10000
    });
    this.setData({
      sayImg: '/images/saying.png'
    })
  },
  endStreamRecord: function () {
    manager.stop();
    this.setData({
      sayImg: '/images/say.png'
    })
  },

  initRecord: function () {
    //有新的识别内容返回，则会调用此事件
    manager.onRecognize = (res) => {
      let text = res.result
      this.setData({
        textareaValue: text,
      })
    }
    // 识别结束事件
    manager.onStop = (res) => {
      let text = res.result
      if (text == '') {
        // 用户没有说话，可以做一下提示处理...
        return
      }
      this.setData({
        textareaValue: text,
      })
      // 得到完整识别内容就可以去翻译了
      this.translateTextAction()
    }
  },
  translateTextAction: function () { },

  onLoad:function() {
    this.initRecord();
    var that = this;
    wx.request({
      method: 'GET',
      url: 'https://xuexi.catni.cn/banner',
      success: function(res){
        console.log(res);
        that.setData({
          swiperList: res.data.data
        })
        console.log(that.data.swiperList);
      }
    });
    // wx.setClipboardData({
    //   data: 'data',
    //   success (res) {
    //     wx.getClipboardData({
    //       success (res) {
    //         console.log(res.data) // data
    //       }
    //     })
    //   }
    // });
    wx.getClipboardData({
      success: function (res) {
        if (res.data) {
          that.setData({
            ClipboardType: true,
            ClipboardValue: res.data
          })
        } else {
          that.setData({
            ClipboardType: false
          })
        }
      }
    });
    wx.request({
      method: 'GET',
      url: 'https://xuexi.catni.cn/basic',
      success: function (res) {
        that.setData({
          res_total: res.data.data.question_total
        })
      }
    })
    this.towerSwiper('swiperList');
    // 初始化towerSwiper 传已有的数组名即可
    
  },
  DotStyle(e) {
    this.setData({
      DotStyle: e.detail.value
    })
  },
  loadProgress(){
    this.setData({
      loadProgress: this.data.loadProgress+5
    })
    console.log(this.data.loadProgress)
    if (this.data.loadProgress<100){
      setTimeout(() => {
        this.loadProgress();
      }, 100)
    }else{
      this.setData({
        loadProgress: 0
      })
    }
  },
  // cardSwiper
  cardSwiper(e) {
    this.setData({
      cardCur: e.detail.current
    })
  },
  // towerSwiper
  // 初始化towerSwiper
  towerSwiper(name) {
    let list = this.data[name];
    for (let i = 0; i < list.length; i++) {
      list[i].zIndex = parseInt(list.length / 2) + 1 - Math.abs(i - parseInt(list.length / 2))
      list[i].mLeft = i - parseInt(list.length / 2)
    }
    this.setData({
      swiperList: list
    })
  },
  // towerSwiper触摸开始
  towerStart(e) {
    this.setData({
      towerStart: e.touches[0].pageX
    })
  },
  // towerSwiper计算方向
  towerMove(e) {
    this.setData({
      direction: e.touches[0].pageX - this.data.towerStart > 0 ? 'right' : 'left'
    })
  },
  // towerSwiper计算滚动
  towerEnd(e) {
    let direction = this.data.direction;
    let list = this.data.swiperList;
    if (direction == 'right') {
      let mLeft = list[0].mLeft;
      let zIndex = list[0].zIndex;
      for (let i = 1; i < list.length; i++) {
        list[i - 1].mLeft = list[i].mLeft
        list[i - 1].zIndex = list[i].zIndex
      }
      list[list.length - 1].mLeft = mLeft;
      list[list.length - 1].zIndex = zIndex;
      this.setData({
        swiperList: list
      })
    } else {
      let mLeft = list[list.length - 1].mLeft;
      let zIndex = list[list.length - 1].zIndex;
      for (let i = list.length - 1; i > 0; i--) {
        list[i].mLeft = list[i - 1].mLeft
        list[i].zIndex = list[i - 1].zIndex
      }
      list[0].mLeft = mLeft;
      list[0].zIndex = zIndex;
      this.setData({
        swiperList: list
      })
    }
  },
  numSteps() {
    this.setData({
      num: this.data.num == this.data.numList.length - 1 ? 0 : this.data.num + 1
    })
  },
  textareaInput(e) {
    // console.log(e)
    this.setData({
      textareaValue: e.detail.value
    })
  },
  
  clear() {
    this.setData({
      textareaValue: '',
      isBindExpert: true,
      arrList: ''
    });
    // console.log(this.data.textareaValue)
  },

  SearchType(e) {
    this.setData({
      SearchTypeValue: e.detail.value
    })
    // console.log(this.data.SearchTypeValue)
  },
  search() {
    var that = this;
    var textvalue = this.data.textareaValue;
    this.loadProgress()
    if (textvalue.length>=2){
      wx.request({
        method: 'GET',
        url: 'https://xuexi.catni.cn/search',
        data: {
          kw: this.data.textareaValue,
          choice: this.data.SearchTypeValue
        },
        success: function (res) {
          console.log(res);
          var total = res.data.data.length;
          console.log(total);
          if (total !== 0) {
            that.setData({
              isBindExpert: false
            })
          } else {
            that.showModal('resModal')
            that.setData({
              isBindExpert: true
            })
          };
          that.setData({
            arrList: res.data.data
          })
        }
      })
    }
    else{
      that.showModal('textareaModal')
    }
  },
  showModal:function(e) {
    console.log(e)
    this.setData({
      modalName: e
    })
  },
  hideModal(e) {
    this.setData({
      modalName: null,
      ClipboardType: null
    })
  },
  Paste(e){
    var that = this
    this.setData({
      ClipboardType: null,
    });
    wx.getClipboardData({
      success (res){
        that.setData({
          textareaValue: res.data,
        });
      }
    })
  },
  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  },  // 获取滚动条当前位置
  onPageScroll: function (e) {
    // console.log(e)
    if (e.scrollTop > 100) {
      this.setData({
        floorstatus: true
      });
    } else {
      this.setData({
        floorstatus: false
      });
    }
  },

  //回到顶部
  goTop: function (e) {  // 一键回到顶部
    if (wx.pageScrollTo) {
      wx.pageScrollTo({
        scrollTop: 0
      })
    } else {
      wx.showModal({
        title: '提示',
        content: '当前微信版本过低，无法使用该功能，请升级到最新微信版本后重试。'
      })
    }
  },
  
})

