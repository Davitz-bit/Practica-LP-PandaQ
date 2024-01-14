# Generated from exprs.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,89,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,
        0,3,0,15,8,0,1,1,1,1,1,1,3,1,20,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,40,8,1,10,1,12,1,
        43,9,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,72,8,3,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,87,8,4,1,4,0,
        1,2,5,0,2,4,6,8,0,0,99,0,14,1,0,0,0,2,19,1,0,0,0,4,44,1,0,0,0,6,
        71,1,0,0,0,8,86,1,0,0,0,10,15,3,2,1,0,11,15,3,4,2,0,12,15,3,6,3,
        0,13,15,3,8,4,0,14,10,1,0,0,0,14,11,1,0,0,0,14,12,1,0,0,0,14,13,
        1,0,0,0,15,1,1,0,0,0,16,17,6,1,-1,0,17,20,5,19,0,0,18,20,5,21,0,
        0,19,16,1,0,0,0,19,18,1,0,0,0,20,41,1,0,0,0,21,22,10,8,0,0,22,23,
        5,1,0,0,23,40,3,2,1,8,24,25,10,7,0,0,25,26,5,2,0,0,26,40,3,2,1,8,
        27,28,10,6,0,0,28,29,5,3,0,0,29,40,3,2,1,7,30,31,10,5,0,0,31,32,
        5,4,0,0,32,40,3,2,1,6,33,34,10,4,0,0,34,35,5,5,0,0,35,40,3,2,1,5,
        36,37,10,3,0,0,37,38,5,6,0,0,38,40,3,2,1,4,39,21,1,0,0,0,39,24,1,
        0,0,0,39,27,1,0,0,0,39,30,1,0,0,0,39,33,1,0,0,0,39,36,1,0,0,0,40,
        43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,3,1,0,0,0,43,41,1,0,0,
        0,44,45,5,7,0,0,45,46,3,2,1,0,46,5,1,0,0,0,47,48,3,2,1,0,48,49,5,
        8,0,0,49,50,3,2,1,0,50,72,1,0,0,0,51,52,3,2,1,0,52,53,5,9,0,0,53,
        54,3,2,1,0,54,72,1,0,0,0,55,56,3,2,1,0,56,57,5,10,0,0,57,58,3,2,
        1,0,58,72,1,0,0,0,59,60,3,2,1,0,60,61,5,11,0,0,61,62,3,2,1,0,62,
        72,1,0,0,0,63,64,3,2,1,0,64,65,5,12,0,0,65,66,3,2,1,0,66,72,1,0,
        0,0,67,68,3,2,1,0,68,69,5,13,0,0,69,70,3,2,1,0,70,72,1,0,0,0,71,
        47,1,0,0,0,71,51,1,0,0,0,71,55,1,0,0,0,71,59,1,0,0,0,71,63,1,0,0,
        0,71,67,1,0,0,0,72,7,1,0,0,0,73,74,5,14,0,0,74,75,3,6,3,0,75,76,
        5,15,0,0,76,77,3,4,2,0,77,78,5,16,0,0,78,87,1,0,0,0,79,80,5,17,0,
        0,80,81,3,6,3,0,81,82,5,18,0,0,82,83,3,4,2,0,83,84,3,2,1,0,84,85,
        5,16,0,0,85,87,1,0,0,0,86,73,1,0,0,0,86,79,1,0,0,0,87,9,1,0,0,0,
        6,14,19,39,41,71,86
    ]

class exprsParser ( Parser ):

    grammarFileName = "exprs.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'^'", "'*'", "'/'", "'+'", "'-'", "':='", 
                     "'write'", "'<'", "'<='", "'>'", "'>='", "'='", "'<>'", 
                     "'if'", "'then'", "'end'", "'while'", "'do'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUM", "WS", 
                      "WORD" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_act = 2
    RULE_comp = 3
    RULE_ctrl = 4

    ruleNames =  [ "root", "expr", "act", "comp", "ctrl" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    NUM=19
    WS=20
    WORD=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)


        def act(self):
            return self.getTypedRuleContext(exprsParser.ActContext,0)


        def comp(self):
            return self.getTypedRuleContext(exprsParser.CompContext,0)


        def ctrl(self):
            return self.getTypedRuleContext(exprsParser.CtrlContext,0)


        def getRuleIndex(self):
            return exprsParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = exprsParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.state = 14
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.act()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 12
                self.comp()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 13
                self.ctrl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprsParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SumaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuma" ):
                return visitor.visitSuma(self)
            else:
                return visitor.visitChildren(self)


    class PotenciaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPotencia" ):
                return visitor.visitPotencia(self)
            else:
                return visitor.visitChildren(self)


    class AssignacioContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignacio" ):
                return visitor.visitAssignacio(self)
            else:
                return visitor.visitChildren(self)


    class NumeroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(exprsParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicacioContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicacio" ):
                return visitor.visitMultiplicacio(self)
            else:
                return visitor.visitChildren(self)


    class RestaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResta" ):
                return visitor.visitResta(self)
            else:
                return visitor.visitChildren(self)


    class DivisioContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivisio" ):
                return visitor.visitDivisio(self)
            else:
                return visitor.visitChildren(self)


    class ParaulaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WORD(self):
            return self.getToken(exprsParser.WORD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParaula" ):
                return visitor.visitParaula(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = exprsParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                localctx = exprsParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 17
                self.match(exprsParser.NUM)
                pass
            elif token in [21]:
                localctx = exprsParser.ParaulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 18
                self.match(exprsParser.WORD)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 39
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = exprsParser.PotenciaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 21
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 22
                        self.match(exprsParser.T__0)
                        self.state = 23
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = exprsParser.MultiplicacioContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 24
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 25
                        self.match(exprsParser.T__1)
                        self.state = 26
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = exprsParser.DivisioContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 27
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 28
                        self.match(exprsParser.T__2)
                        self.state = 29
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = exprsParser.SumaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 30
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 31
                        self.match(exprsParser.T__3)
                        self.state = 32
                        self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = exprsParser.RestaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 33
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 34
                        self.match(exprsParser.T__4)
                        self.state = 35
                        self.expr(5)
                        pass

                    elif la_ == 6:
                        localctx = exprsParser.AssignacioContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 36
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 37
                        self.match(exprsParser.T__5)
                        self.state = 38
                        self.expr(4)
                        pass

             
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ActContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprsParser.RULE_act

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EscriureContext(ActContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ActContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEscriure" ):
                return visitor.visitEscriure(self)
            else:
                return visitor.visitChildren(self)



    def act(self):

        localctx = exprsParser.ActContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_act)
        try:
            localctx = exprsParser.EscriureContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(exprsParser.T__6)
            self.state = 45
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprsParser.RULE_comp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MenorigualContext(CompContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.CompContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMenorigual" ):
                return visitor.visitMenorigual(self)
            else:
                return visitor.visitChildren(self)


    class MajorContext(CompContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.CompContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMajor" ):
                return visitor.visitMajor(self)
            else:
                return visitor.visitChildren(self)


    class MenorContext(CompContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.CompContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMenor" ):
                return visitor.visitMenor(self)
            else:
                return visitor.visitChildren(self)


    class IgualContext(CompContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.CompContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgual" ):
                return visitor.visitIgual(self)
            else:
                return visitor.visitChildren(self)


    class DiferentContext(CompContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.CompContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiferent" ):
                return visitor.visitDiferent(self)
            else:
                return visitor.visitChildren(self)


    class MajorigualContext(CompContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.CompContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMajorigual" ):
                return visitor.visitMajorigual(self)
            else:
                return visitor.visitChildren(self)



    def comp(self):

        localctx = exprsParser.CompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_comp)
        try:
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = exprsParser.MenorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.expr(0)
                self.state = 48
                self.match(exprsParser.T__7)
                self.state = 49
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = exprsParser.MenorigualContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.expr(0)
                self.state = 52
                self.match(exprsParser.T__8)
                self.state = 53
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = exprsParser.MajorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.expr(0)
                self.state = 56
                self.match(exprsParser.T__9)
                self.state = 57
                self.expr(0)
                pass

            elif la_ == 4:
                localctx = exprsParser.MajorigualContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 59
                self.expr(0)
                self.state = 60
                self.match(exprsParser.T__10)
                self.state = 61
                self.expr(0)
                pass

            elif la_ == 5:
                localctx = exprsParser.IgualContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 63
                self.expr(0)
                self.state = 64
                self.match(exprsParser.T__11)
                self.state = 65
                self.expr(0)
                pass

            elif la_ == 6:
                localctx = exprsParser.DiferentContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 67
                self.expr(0)
                self.state = 68
                self.match(exprsParser.T__12)
                self.state = 69
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CtrlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprsParser.RULE_ctrl

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MentreContext(CtrlContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.CtrlContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def comp(self):
            return self.getTypedRuleContext(exprsParser.CompContext,0)

        def act(self):
            return self.getTypedRuleContext(exprsParser.ActContext,0)

        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMentre" ):
                return visitor.visitMentre(self)
            else:
                return visitor.visitChildren(self)


    class CondicionalContext(CtrlContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.CtrlContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def comp(self):
            return self.getTypedRuleContext(exprsParser.CompContext,0)

        def act(self):
            return self.getTypedRuleContext(exprsParser.ActContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)



    def ctrl(self):

        localctx = exprsParser.CtrlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ctrl)
        try:
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                localctx = exprsParser.CondicionalContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.match(exprsParser.T__13)
                self.state = 74
                self.comp()
                self.state = 75
                self.match(exprsParser.T__14)
                self.state = 76
                self.act()
                self.state = 77
                self.match(exprsParser.T__15)
                pass
            elif token in [17]:
                localctx = exprsParser.MentreContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.match(exprsParser.T__16)
                self.state = 80
                self.comp()
                self.state = 81
                self.match(exprsParser.T__17)
                self.state = 82
                self.act()
                self.state = 83
                self.expr(0)
                self.state = 84
                self.match(exprsParser.T__15)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         




