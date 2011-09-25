About
=====
リスト内のDBRef全部にクエリを発行せずに{$in: [1,2,...,n]}する。


Example
=======
使い方は簡単で、AutoReferenceをimportしたあとにimportするだけです。

>>> from pymongo.son_manipulator import AutoReference, NamespaceInjector
>>> import autoreference_patch