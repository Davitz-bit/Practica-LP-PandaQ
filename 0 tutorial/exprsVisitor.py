# Generated from exprs.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .exprsParser import exprsParser
else:
    from exprsParser import exprsParser

# This class defines a complete generic visitor for a parse tree produced by exprsParser.

class exprsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by exprsParser#root.
    def visitRoot(self, ctx:exprsParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#suma.
    def visitSuma(self, ctx:exprsParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#potencia.
    def visitPotencia(self, ctx:exprsParser.PotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#assignacio.
    def visitAssignacio(self, ctx:exprsParser.AssignacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#numero.
    def visitNumero(self, ctx:exprsParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#multiplicacio.
    def visitMultiplicacio(self, ctx:exprsParser.MultiplicacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#resta.
    def visitResta(self, ctx:exprsParser.RestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#divisio.
    def visitDivisio(self, ctx:exprsParser.DivisioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#paraula.
    def visitParaula(self, ctx:exprsParser.ParaulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#escriure.
    def visitEscriure(self, ctx:exprsParser.EscriureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#menor.
    def visitMenor(self, ctx:exprsParser.MenorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#menorigual.
    def visitMenorigual(self, ctx:exprsParser.MenorigualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#major.
    def visitMajor(self, ctx:exprsParser.MajorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#majorigual.
    def visitMajorigual(self, ctx:exprsParser.MajorigualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#igual.
    def visitIgual(self, ctx:exprsParser.IgualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#diferent.
    def visitDiferent(self, ctx:exprsParser.DiferentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#condicional.
    def visitCondicional(self, ctx:exprsParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#mentre.
    def visitMentre(self, ctx:exprsParser.MentreContext):
        return self.visitChildren(ctx)



del exprsParser